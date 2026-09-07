from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "project_context.md"

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
    "project_context.md",
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
        p
        for p in ROOT.rglob("*")
        if p.is_file() and should_include(p)
    ]

    # Sắp xếp để project context có cấu trúc ổn định
    files.sort(key=lambda p: str(p.relative_to(ROOT)))

    with OUTPUT.open("w", encoding="utf-8") as out:

        # =========================================================
        # PROJECT CONTEXT
        # =========================================================

        out.write("# PROJECT CONTEXT\n\n")

        out.write(f"**Project root:** `{ROOT}`  \n")
        out.write(f"**Total included files:** {len(files)}\n\n")

        # =========================================================
        # 1. PROJECT STRUCTURE
        # =========================================================

        out.write("## Project Structure\n\n")

        for file in files:
            relative = file.relative_to(ROOT)
            out.write(f"- `{relative}`\n")

        # =========================================================
        # 2. FILE CONTENTS
        # =========================================================

        out.write("\n## File Contents\n")

        for file in files:
            relative = file.relative_to(ROOT)

            out.write("\n\n")
            out.write("---\n\n")
            out.write(f"## `{relative}`\n\n")

            try:
                content = file.read_text(encoding="utf-8")

                # Xác định ngôn ngữ cho Markdown code fence
                suffix = file.suffix.lower()

                language_map = {
                    ".py": "python",
                    ".md": "markdown",
                    ".txt": "text",
                    ".ini": "ini",
                    ".yml": "yaml",
                    ".yaml": "yaml",
                    ".sh": "bash",
                    ".dockerfile": "dockerfile",
                }

                language = language_map.get(suffix, "")

                # Các file không có extension
                if file.name == "Dockerfile":
                    language = "dockerfile"
                elif file.name in {".gitignore", ".dockerignore"}:
                    language = "gitignore"
                elif file.name == "LICENSE":
                    language = "text"

                out.write(f"```{language}\n")
                out.write(content)

                # Đảm bảo code fence không dính vào nội dung file
                if not content.endswith("\n"):
                    out.write("\n")

                out.write("```\n")

            except UnicodeDecodeError:
                out.write(
                    "[Could not decode this file as UTF-8]\n"
                )

            except Exception as e:
                out.write(
                    f"[Could not read file: {e}]\n"
                )

    print("Done!")
    print(f"Included files: {len(files)}")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()

