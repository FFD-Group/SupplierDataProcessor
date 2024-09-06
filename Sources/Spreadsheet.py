from Sources.FileType import FileType

SPREADSHEET_FILE_TYPE = "{} Spreadsheet"


class Spreadsheet(FileType):
    """Represents a spreadsheet file on the OS being
    used as a source for supplier item data."""

    def getFileType(self) -> str:
        """Return the file type."""
        return SPREADSHEET_FILE_TYPE.format(self.file_type)
