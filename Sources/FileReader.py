from typing import List
from Sources import FileType


class FileReader:
    """The FileReader class will read a source file and
    obtain the str representations of an item."""

    file: FileType
    read_file_items: List[str]

    def readFile(file: FileType) -> List[str]:
        """Read the item representations from the file."""

        raise NotImplementedError
