#!/usr/bin/env python3
"""Create a prioritized, size-limited and secret-redacted project_context.md.

Usage:
    python build_project_context.py
    python build_project_context.py --root . --output project_context.md
    python build_project_context.py --max-total-chars 450000

Standard library only. Put this script in the project root for the simplest use.
"""
from __future__ import annotations

import argparse
import fnmatch
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

VERSION = "2.0"

EXCLUDED_DIRS = {
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".hypothesis", ".tox", ".nox", ".venv", "venv", "env", "node_modules",
    ".next", ".nuxt", ".turbo", ".vercel", ".netlify", "dist", "build",
    "coverage", "htmlcov", ".cache", ".idea", ".vscode", ".terraform",
    ".serverless", "site-packages", "vendor", "target", "logs", ".ssh",
    ".aws", ".azure", ".kube", "certificates", "certs",
}

# .sql is essential for PostgreSQL projects and is deliberately included.
ALLOWED_EXTENSIONS = {
    ".py", ".pyi", ".sql", ".md", ".mdx", ".rst", ".txt", ".ini",
    ".cfg", ".toml", ".yaml", ".yml", ".json", ".sh", ".bash", ".ps1",
    ".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".html", ".xml", ".css",
    ".dockerfile",
}
ALLOWED_FILENAMES = {
    "Dockerfile", "LICENSE", "Makefile", "Procfile", "Pipfile", "Justfile",
    "Taskfile", "alembic.ini", ".gitignore", ".dockerignore", ".editorconfig",
}
EXCLUDED_FILENAMES = {
    "project_context.md", "package-lock.json", "npm-shrinkwrap.json", "yarn.lock",
    "pnpm-lock.yaml", "poetry.lock", "uv.lock", "Pipfile.lock", ".DS_Store",
    "Thumbs.db",
}
EXCLUDED_PATTERNS = {
    "*.lock", "*.log", "*.pyc", "*.pyo", "*.pyd", "*.so", "*.dll", "*.exe",
    "*.bin", "*.db", "*.sqlite", "*.sqlite3", "*.parquet", "*.csv", "*.tsv",
    "*.xlsx", "*.xls", "*.pdf", "*.zip", "*.7z", "*.tar", "*.gz", "*.png",
    "*.jpg", "*.jpeg", "*.gif", "*.webp", "*.ico", "*.mp3", "*.mp4", "*.mov",
    "*.woff", "*.woff2", "*.ttf", "*.otf", "*.map", "*.min.js", "*.min.css",
    "*.generated.*",
}
SENSITIVE_FILENAME_PATTERNS = {
    ".env*", "*credentials*", "*service-account*", "*private-key*", "id_rsa*",
    "id_ed25519*", "*.pem", "*.key", "*.p12", "*.pfx", "*.crt", "*.cer", "*.der",
}

SECRET_NAME = (
    r"[\w.-]*(?:PASSWORD|PASSWD|SECRET|TOKEN|API[_-]?KEY|PRIVATE[_-]?KEY|"
    r"DATABASE_URL|DB_URL|DSN|CONNECTION_STRING|CLIENT_SECRET|ACCESS_KEY)[\w.-]*"
)
QUOTED_SECRET_RE = re.compile(
    rf"(?i)(?P<prefix>[\"']?{SECRET_NAME}[\"']?\s*[:=]\s*)"
    r"(?P<quote>[\"'])(?P<value>.*?)(?P=quote)"
)
UNQUOTED_SECRET_RE = re.compile(
    rf"(?i)(?P<prefix>\b{SECRET_NAME}\b\s*[:=]\s*)"
    r"(?P<value>(?![\"'])([^\s,;#]+))"
)
PEM_RE = re.compile(
    r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----.*?"
    r"-----END (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", re.DOTALL
)
BEARER_RE = re.compile(r"(?i)\b(Bearer\s+)[A-Za-z0-9._~+/=-]+")
URL_PASSWORD_RE = re.compile(
    r"(?i)(https?://[^:/\s]+:|postgres(?:ql)?://[^:/\s]+:)([^@\s/]+)(@)"
)
JWT_RE = re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")
TOKEN_PATTERNS = [
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
]
LANGUAGES = {
    ".py": "python", ".pyi": "python", ".sql": "sql", ".md": "markdown",
    ".mdx": "mdx", ".rst": "rst", ".txt": "text", ".ini": "ini",
    ".cfg": "ini", ".toml": "toml", ".yaml": "yaml", ".yml": "yaml",
    ".json": "json", ".sh": "bash", ".bash": "bash", ".ps1": "powershell",
    ".js": "javascript", ".jsx": "jsx", ".mjs": "javascript", ".cjs": "javascript",
    ".ts": "typescript", ".tsx": "tsx", ".html": "html", ".xml": "xml",
    ".css": "css", ".dockerfile": "dockerfile",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a safe project context Markdown file.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent,
                        help="Project root; defaults to the folder containing this script.")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output path; defaults to <root>/project_context.md.")
    parser.add_argument("--max-file-mb", type=float, default=0.30,
                        help="Skip individual files larger than this size; default 0.30 MB.")
    parser.add_argument("--max-file-chars", type=int, default=60000,
                        help="Maximum characters included from one file; default 60000.")
    parser.add_argument("--max-total-chars", type=int, default=350000,
                        help="Maximum combined source-content characters; default 350000.")
    return parser.parse_args()


def is_inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def should_include(path: Path, root: Path, output: Path) -> bool:
    if path.is_symlink():
        return False
    try:
        resolved = path.resolve()
        if resolved == output or not is_inside(resolved, root):
            return False
    except OSError:
        return False

    relative_parts = path.relative_to(root).parts
    if any(part.lower() in EXCLUDED_DIRS for part in relative_parts[:-1]):
        return False

    name = path.name
    lower_name = name.lower()
    suffix = path.suffix.lower()

    # Exclude every .env variant, not just a file literally named .env.
    if lower_name.startswith(".env"):
        return False
    if lower_name in {item.lower() for item in EXCLUDED_FILENAMES}:
        return False
    if any(fnmatch.fnmatch(lower_name, p) for p in SENSITIVE_FILENAME_PATTERNS):
        return False
    if any(fnmatch.fnmatch(lower_name, p) for p in EXCLUDED_PATTERNS):
        return False
    if suffix in ALLOWED_EXTENSIONS:
        return True
    if name in ALLOWED_FILENAMES or lower_name in {x.lower() for x in ALLOWED_FILENAMES}:
        return True
    return lower_name.startswith("requirements") and suffix == ".txt"


def priority_for(relative: str) -> int:
    """Lower score means earlier inclusion when the context budget is limited."""
    path = relative.lower()
    parts = set(path.split("/"))
    filename = path.rsplit("/", 1)[-1]

    if filename in {
        "readme.md", "pyproject.toml", "requirements.txt", "docker-compose.yml",
        "docker-compose.yaml", "compose.yml", "compose.yaml", "alembic.ini",
    }:
        return 0
    if filename in {"main.py", "database.py", "db.py", "config.py", "settings.py"}:
        return 1
    if parts.intersection({
        "models", "schemas", "routers", "routes", "repositories", "services",
        "crud", "dependencies", "migrations", "versions", "sql", "analytics",
    }):
        return 1
    if "tests" in parts:
        return 2
    if "mentor-web" in parts or ".github" in parts:
        return 3
    if "docs" in parts:
        return 4
    return 3


def collect_files(root: Path, output: Path) -> List[Dict[str, object]]:
    records: List[Dict[str, object]] = []
    for current, directories, filenames in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        directories[:] = sorted(
            d for d in directories
            if d.lower() not in EXCLUDED_DIRS and not (current_path / d).is_symlink()
        )
        for filename in sorted(filenames):
            path = current_path / filename
            if not should_include(path, root, output):
                continue
            try:
                size = path.stat().st_size
            except OSError:
                continue
            relative = path.relative_to(root).as_posix()
            records.append({
                "path": path,
                "relative": relative,
                "size": size,
                "priority": priority_for(relative),
            })
    records.sort(key=lambda x: (int(x["priority"]), str(x["relative"]).lower()))
    return records


def redact_secrets(content: str) -> Tuple[str, int]:
    """Best-effort redaction; no automatic scanner can guarantee secret detection."""
    count_total = 0

    def quoted_replacement(match: re.Match) -> str:
        return match.group("prefix") + match.group("quote") + "[REDACTED]" + match.group("quote")

    content, count = QUOTED_SECRET_RE.subn(quoted_replacement, content)
    count_total += count

    safe_rhs = (
        "os.getenv", "os.environ", "environ[", "settings.", "config.", "secretstr",
        "field(", "${", "$", "none", "null", "true", "false", "required",
    )

    def unquoted_replacement(match: re.Match) -> str:
        nonlocal count_total
        value = match.group("value")
        if value.lower().startswith(safe_rhs):
            return match.group(0)
        count_total += 1
        return match.group("prefix") + "[REDACTED]"

    content = UNQUOTED_SECRET_RE.sub(unquoted_replacement, content)
    for pattern, replacement in (
        (PEM_RE, "[REDACTED PRIVATE KEY BLOCK]"),
        (BEARER_RE, r"\1[REDACTED]"),
        (URL_PASSWORD_RE, r"\1[REDACTED]\3"),
        (JWT_RE, "[REDACTED JWT]"),
    ):
        content, count = pattern.subn(replacement, content)
        count_total += count
    for pattern in TOKEN_PATTERNS:
        content, count = pattern.subn("[REDACTED TOKEN]", content)
        count_total += count
    return content, count_total


def read_text_file(path: Path) -> Tuple[Optional[str], Optional[str]]:
    try:
        raw = path.read_bytes()
    except OSError as error:
        return None, f"read error: {error}"
    if b"\x00" in raw:
        return None, "binary file detected"
    try:
        return raw.decode("utf-8-sig"), None
    except UnicodeDecodeError:
        return None, "not valid UTF-8 text"


def truncate_text(content: str, limit: int) -> Tuple[str, bool]:
    if len(content) <= limit:
        return content, False
    marker = "\n\n[... CONTENT TRUNCATED BY PROJECT CONTEXT BUILDER ...]\n\n"
    if limit <= len(marker) + 20:
        return content[:limit], True
    available = limit - len(marker)
    head_size = int(available * 0.75)
    tail_size = available - head_size
    head = content[:head_size]
    tail = content[-tail_size:]
    if "\n" in head:
        head = head.rsplit("\n", 1)[0]
    if "\n" in tail:
        tail = tail.split("\n", 1)[-1]
    return head + marker + tail, True


def make_fence(content: str) -> str:
    runs = re.findall(r"`+", content)
    longest = max((len(run) for run in runs), default=0)
    return "`" * max(3, longest + 1)


def language_for(path: Path) -> str:
    if path.name.lower() == "dockerfile":
        return "dockerfile"
    if path.name.lower() in {".gitignore", ".dockerignore"}:
        return "gitignore"
    if path.name.lower() == "license":
        return "text"
    return LANGUAGES.get(path.suffix.lower(), "")


def render_file_block(record: Dict[str, object], content: str,
                      redactions: int, truncated: bool) -> str:
    path = record["path"]
    assert isinstance(path, Path)
    relative = str(record["relative"])
    fence = make_fence(content)
    lines = content.count("\n") + (1 if content else 0)
    metadata = (
        f"**Size:** {int(record['size']):,} bytes | **Lines included:** {lines:,} | "
        f"**Secret values redacted:** {redactions}"
    )
    if truncated:
        metadata += " | **Note:** content truncated to respect context limits"
    ending = "" if content.endswith("\n") else "\n"
    return (
        f"\n\n---\n\n## File: `{relative}`\n\n{metadata}\n\n"
        f"{fence}{language_for(path)}\n{content}{ending}{fence}\n"
    )


def git_info(root: Path) -> str:
    try:
        branch = subprocess.run(
            ["git", "-C", str(root), "branch", "--show-current"],
            capture_output=True, text=True, timeout=3, check=False,
        )
        commit = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=3, check=False,
        )
        b = branch.stdout.strip() if branch.returncode == 0 else ""
        c = commit.stdout.strip() if commit.returncode == 0 else ""
        if not b and not c:
            return "Git metadata: unavailable"
        return f"Git branch: `{b or 'unknown'}`  \nGit commit: `{c or 'unknown'}`"
    except (OSError, subprocess.SubprocessError):
        return "Git metadata: unavailable"


def build_report(root: Path, records: List[Dict[str, object]], max_file_bytes: int,
                 max_file_chars: int, max_total_chars: int) -> Tuple[str, Dict[str, int]]:
    blocks: List[str] = []
    omitted: List[Tuple[str, str]] = []
    included = redaction_total = truncated_total = content_chars = included_bytes = 0

    for record in records:
        relative = str(record["relative"])
        size = int(record["size"])
        if size > max_file_bytes:
            omitted.append((relative, f"file too large ({size:,} bytes)"))
            continue
        content, error = read_text_file(record["path"])  # type: ignore[arg-type]
        if error:
            omitted.append((relative, error))
            continue
        assert content is not None
        content, redactions = redact_secrets(content)
        content, truncated = truncate_text(content, max_file_chars)
        block = render_file_block(record, content, redactions, truncated)
        if content_chars + len(block) > max_total_chars:
            omitted.append((relative, "total context character budget reached"))
            continue
        blocks.append(block)
        content_chars += len(block)
        included += 1
        included_bytes += size
        redaction_total += redactions
        truncated_total += int(truncated)

    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    header = f"""# PROJECT CONTEXT

> Generated by `build_project_context.py` v{VERSION}. This is a repository snapshot, not a live connection.

## Snapshot Metadata

- **Project:** `{root.name}`
- **Generated at:** `{timestamp}`
- **Candidate files discovered:** {len(records)}
- **Files included:** {included}
- **Files omitted:** {len(omitted)}
- **Original size of included files:** {included_bytes:,} bytes
- **Source content included:** {content_chars:,} characters
- **Secret-like values redacted:** {redaction_total}
- **Files truncated:** {truncated_total}
- **Maximum source-content budget:** {max_total_chars:,} characters

{git_info(root)}

## Instructions for the AI Assistant

1. Treat the paths and source contents below as the repository snapshot at generation time.
2. Do not assume an omitted file, endpoint, table, column, dependency, or feature exists.
3. Follow the project's existing architecture, naming conventions, and dependency choices.
4. For database questions, inspect SQL files, ORM models, schemas, and migrations together when available.
5. Do not invent database columns, API routes, environment variables, or test results.
6. Distinguish verified source-code facts from assumptions and recommendations.
7. Never ask the user to publish passwords, API keys, tokens, private keys, or `.env` contents.
8. This snapshot can become outdated; request a fresh one when the current repository state matters.
9. Do not edit this generated context file as if it were source code; edit the original project files.

## Project File Inventory

Files are ordered by relevance: configuration and entry points, core application/database code, tests, frontend, then documentation.

"""
    inventory = "\n".join(
        f"- `{r['relative']}` ({int(r['size']):,} bytes; priority {r['priority']})"
        for r in records
    ) or "- No eligible text files were found."
    omitted_text = ""
    if omitted:
        omitted_text = "\n\n## Omitted Files and Reasons\n\n" + "\n".join(
            f"- `{name}` — {reason}" for name, reason in omitted
        )
    report = (
        header + inventory + omitted_text + "\n\n## Source File Contents\n"
        + "".join(blocks) + "\n\n---\n\n## End of Project Context\n"
    )
    return report, {
        "discovered": len(records), "included": included, "omitted": len(omitted),
        "redactions": redaction_total, "truncated": truncated_total,
        "content_chars": content_chars, "included_bytes": included_bytes,
    }


def main() -> None:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"ERROR: Project root is not a directory: {root}")

    if args.output is None:
        output = root / "project_context.md"
    else:
        output = args.output.expanduser()
        if not output.is_absolute():
            output = root / output
        output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    if args.max_file_mb <= 0 or args.max_file_chars <= 0 or args.max_total_chars <= 0:
        raise SystemExit("ERROR: All size limits must be greater than zero.")

    print("Scanning project files...")
    records = collect_files(root, output)
    print("Prioritizing source files and redacting common secret patterns...")
    report, stats = build_report(
        root, records, int(args.max_file_mb * 1024 * 1024),
        args.max_file_chars, args.max_total_chars,
    )
    output.write_text(report, encoding="utf-8")

    print("\nDone!")
    print(f"Project root:       {root}")
    print(f"Output:             {output}")
    print(f"Files discovered:   {stats['discovered']}")
    print(f"Files included:     {stats['included']}")
    print(f"Files omitted:      {stats['omitted']}")
    print(f"Secret redactions:  {stats['redactions']}")
    print(f"Files truncated:    {stats['truncated']}")
    print(f"Context characters: {len(report):,}")
    print("\nReview the generated Markdown before uploading it.")
    print("Secret redaction is best-effort; never store real credentials in source files.")


if __name__ == "__main__":
    main()
