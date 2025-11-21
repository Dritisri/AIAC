from pathlib import Path
from typing import Union
def read_file(filename: Union[str, Path]) -> str:
    """Read and return the full contents of a text file as UTF-8.

    Raises:
        FileNotFoundError: If the path does not exist.
        IsADirectoryError: If the path is a directory.
        UnicodeDecodeError: If the file cannot be decoded as UTF-8.
    """
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if path.is_dir():
        raise IsADirectoryError(f"Expected a file but got directory: {path}")

    with path.open("r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    sample_file = Path(__file__).with_name("sample.txt")
    sample_file.write_text("Hello, world!\nThis is a sample file.\n", encoding="utf-8")
    print("Reading:", sample_file.name)
    print(read_file(sample_file))

    


