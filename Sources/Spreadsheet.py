from Sources import FileType


class Spreadsheet(FileType):
    """Represents a spreadsheet file on the OS being
    used as a source for supplier item data."""

    filename: str
    filepath: str

    def getFilePath(self) -> str:
        """Return the filepath."""

        raise NotImplementedError

    def getFileType(self) -> str:
        """Return the file type."""

        raise NotImplementedError
