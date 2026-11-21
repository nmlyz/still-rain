import os
import tempfile

TEXT = "Past the last streetlight, a field holds the evening still. The grass leans where the wind left it, and one oak keeps the day in its branches. Ants cross a stone the way slow rivers cross a plain. Above them, stars arrive one at a time, each finding a place already waiting."


def validate(text: str) -> None:
    if not text.strip():
        raise ValueError("text must not be only whitespace")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"text must be 1-280 characters, got {len(text)}")
    if text.endswith("\n"):
        raise ValueError("text must not end with a newline")


def write_atomic(path: str, text: str) -> None:
    directory = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    os.chmod(path, 0o644)


def main() -> None:
    validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_atomic(path, TEXT)


if __name__ == "__main__":
    main()
