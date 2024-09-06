from Sources.FileType import FileType

XML_FILE_TYPE = "XML file"


class XMLFile(FileType):
    """Represents an XML file on the OS being used as
    a source for supplier item data."""

    def getFileType(self) -> str:
        """Return the file type."""
        return XML_FILE_TYPE
