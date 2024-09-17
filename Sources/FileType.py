from pathlib import Path
from abc import ABC, abstractmethod
from typing import List
from Sources.SourceProtocol import SourceProtocol

EXTENSION_READER_CLASS_MAP = {
    "XML": "Sources.XMLFile.XMLReader",
    "CSV": "Sources.Spreadsheet.SpreadsheetReader",
}


class FileReader:
    """The FileReader class will read a source file and
    obtain the str representations of its items."""

    @property
    @abstractmethod
    def file(self) -> "FileType":
        pass

    @file.setter
    def file(self, file: "FileType") -> None:
        self._file = file

    @property
    @abstractmethod
    def read_file_items(self) -> List[str]:
        pass

    @read_file_items.setter
    def read_file_items(self, items: List[str]) -> None:
        self._read_file_items = items

    @abstractmethod
    def readFile(
        self, file: "FileType", skiprows: List | int | callable = None
    ) -> List[str]:
        """Read the item representations from the file."""
        pass


class FileType(ABC, SourceProtocol):
    """Base class for different types of source files."""

    @property
    @abstractmethod
    def reader(self):
        pass

    @property
    @abstractmethod
    def file_path(self):
        pass

    def __init__(self, file_path: str, reader: FileReader) -> None:
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
        self.reader = reader

    def getFilePath(self) -> str:
        """Return the file path."""
        return self.file_path

    @abstractmethod
    def getFileType(self) -> str:
        """Return the type of file."""

    @abstractmethod
    def readFile(self) -> List[str]:
        """Read the data from the file and get a list
        of representing item strings."""
        pass
