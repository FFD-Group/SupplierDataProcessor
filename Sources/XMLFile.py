import json
import xml.etree.ElementTree as ET
import xmltodict
from typing import List
from Sources.FileType import FileType, FileReader


XML_FILE_TYPE = "XML file"


class XMLReader(FileReader):

    def __init__(self, item_xml_path="product") -> None:
        self.item_xml_path = item_xml_path

    def readFile(self, file: FileType) -> List[str]:
        read_items = []
        tree = ET.parse(file.getFilePath())
        root = tree.getroot()
        item_path = self.item_xml_path
        for item in root.findall(item_path):
            dict_item = xmltodict.parse(ET.tostring(item, "utf-8"))
            json_item = json.dumps(dict_item[item_path])
            read_items.append(json_item)
        return read_items


class XMLFile(FileType):
    """Represents an XML file on the OS being used as
    a source for supplier item data."""

    @property
    def reader(self) -> XMLReader:
        return self._reader

    @reader.setter
    def reader(self, xml_reader: XMLReader) -> None:
        self._reader = xml_reader

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, path: str) -> None:
        self._file_path = path

    def getFileType(self) -> str:
        """Return the file type."""
        return XML_FILE_TYPE

    def readFile(self) -> List[str]:
        return self.reader.readFile(self)
