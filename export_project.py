from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "project_context.txt"

# Những thư mục không cần đưa cho ChatGPT
EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    "venv",
    ".venv",
    "env",
    ".env",
}

# Những file không cần đưa
EXCLUDED_FILES = {
    ".env",
    ".env.docker",
    "project_context.txt",
}

# Chỉ lấy những loại file có ích cho việc đọc source
ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".ini",
    ".yml",
    ".yaml",
    ".sh",
    ".dockerfile",
}

# Một số file không có extension
ALLOWED_FILENAMES = {
    "Dockerfile",
    "LICENSE",
    ".gitignore",
    ".dockerignore",
}


def should_include(path: Path) -> bool:
    # Loại thư mục
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False

    # Loại file cụ thể
    if path.name in EXCLUDED_FILES:
        return False

    # Loại binary Python
    if path.suffix.lower() in {".pyc", ".pyo", ".so"}:
        return False

    # Chỉ lấy file phù hợp
    if path.name in ALLOWED_FILENAMES:
        return True

    return path.suffix.lower() in ALLOWED_EXTENSIONS


def main():
    files = [
        p for p in ROOT.rglob("*")
        if p.is_file() and should_include(p)
    ]

    # Sắp xếp để project context có cấu trúc ổn định
    files.sort(key=lambda p: str(p.relative_to(ROOT)))

    with OUTPUT.open("w", encoding="utf-8") as out:

        out.write("=" * 80 + "\n")
        out.write("PROJECT CONTEXT\n")
        out.write("=" * 80 + "\n\n")

        out.write(f"Project root: {ROOT}\n")
        out.write(f"Total included files: {len(files)}\n\n")

        # ---------------------------------------------------------
        # 1. PROJECT STRUCTURE
        # ---------------------------------------------------------

        out.write("=" * 80 + "\n")
        out.write("PROJECT STRUCTURE\n")
        out.write("=" * 80 + "\n\n")

        for file in files:
            relative = file.relative_to(ROOT)
            out.write(f"{relative}\n")

        # ---------------------------------------------------------
        # 2. FILE CONTENTS
        # ---------------------------------------------------------

        for file in files:
            relative = file.relative_to(ROOT)

            out.write("\n\n")
            out.write("#" * 80 + "\n")
            out.write(f"FILE: {relative}\n")
            out.write("#" * 80 + "\n\n")

            try:
                content = file.read_text(encoding="utf-8")
                out.write(content)
            except UnicodeDecodeError:
                out.write("[Could not decode this file as UTF-8]\n")
            except Exception as e:
                out.write(f"[Could not read file: {e}]\n")

    print(f"Done!")
    print(f"Included files: {len(files)}")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()

