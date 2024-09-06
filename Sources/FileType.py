from pathlib import Path
from abc import ABC, abstractmethod
from typing import List
from Sources.FileReader import FileReader
from Sources.SourceProtocol import SourceProtocol


class FileType(ABC, SourceProtocol):
    """Base class for different types of source files."""

    reader: FileReader
    file_path: str
    file_type: str

    def __init__(self, file_path: str) -> None:
        """Instantiate a FileType object.

        Keyword arguments:

        @file_path -- the path to the file.
        """
        root_dir = Path(__file__).resolve().parent.parent
        file_object = Path(root_dir / file_path)
        if not file_object.exists():
            raise FileNotFoundError
        self.file_path = file_path
        self.file_type = file_object.suffix.replace(".", "", 1).upper()

    def getFilePath(self) -> str:
        """Return the file path."""
        return self.file_path

    @abstractmethod
    def getFileType(self) -> str:
        """Return the type of file."""

    def readFile(self) -> List[str]:
        """Read the data from the file and get a list
        of representing item strings."""
        return self.reader.readFile(self)
