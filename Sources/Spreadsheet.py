import logging
import pandas as pd
from typing import List
from Sources.FileType import FileType, FileReader

logger = logging.getLogger(__name__)

SPREADSHEET_FILE_TYPE = "{} Spreadsheet"


class SpreadsheetReader(FileReader):

    def readFile(
        self, file: FileType, skiprows: List | int | callable = None
    ) -> List[str] | None:
        read_items = []
        filetype = file.getFileType()
        try:
            match filetype:
                case "XLSX Spreadsheet":
                    df = pd.read_excel(file.getFilePath(), skiprows=skiprows)
                case "CSV Spreadsheet":
                    df = pd.read_csv(file.getFilePath(), skiprows=skiprows)
                case _:
                    raise ValueError
        except ValueError as value_error_exception:
            logger.exception(value_error_exception)
            return None

        for _, row in df.iterrows():
            read_items.append(row.to_json(force_ascii=False))

        return read_items


class Spreadsheet(FileType):
    """Represents a spreadsheet file on the OS being
    used as a source for supplier item data."""

    skiprows: List | int | callable

    def __init__(
        self,
        file_path: str,
        reader: FileReader,
        skiprows: List | int | callable = None,
    ) -> None:
        super().__init__(file_path, reader)
        self.skiprows = skiprows

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
        return self.reader.readFile(file=self, skiprows=self.skiprows)
