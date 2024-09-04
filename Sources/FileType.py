from abc import ABC, abstractmethod
from typing import List
from Sources import SourceProtocol, Reader


class FileType(ABC, SourceProtocol):
    """Base class for different types of source files."""

    reader: Reader

    @abstractmethod
    def getFilePath(self) -> str:
        """Return the file path."""

    @abstractmethod
    def getFileType(self) -> str:
        """Return the type of file."""

    def readFile(self) -> List[str]:
        """Read the data from the file and get a list
        of representing item strings."""
        return self.reader.readFile(self)
