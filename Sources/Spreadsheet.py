from typing import List
from Sources.FileType import FileType, FileReader

SPREADSHEET_FILE_TYPE = "{} Spreadsheet"


class SpreadsheetReader(FileReader):

    def readFile(self, file: FileType) -> List[str]:
        read_items = []
        # use pandas to read the file depending on extension...
        filetype = file.getFileType()
        # CASES:
        #   "XLS Spreadsheet"
        #   "CSV Spreadsheet"
        #   raise ValueError


class Spreadsheet(FileType):
    """Represents a spreadsheet file on the OS being
    used as a source for supplier item data."""

    @property
    def reader(self) -> SpreadsheetReader:
        return self._reader

    @reader.setter
    def reader(self, spreadsheet_reader: SpreadsheetReader) -> None:
        self._reader = spreadsheet_reader

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, path: str) -> None:
        self._file_path = path

    def getFileType(self) -> str:
        """Return the file type."""
        return SPREADSHEET_FILE_TYPE.format(self.file_type)

    def readFile(self) -> List[str]:
        return self.reader.readFile(self)
