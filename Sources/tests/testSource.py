import unittest
from Sources.Source import Source
from Sources.Item import Item
from Sources.XMLFile import XMLFile, XMLReader

EXPECTED_XML_PATH = "files/test_xml_file.xml"


class testSource(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        reader = XMLReader()
        source = XMLFile(EXPECTED_XML_PATH, reader)
        self.source = Source(source)

    def testGetSourcePath(self) -> None:
        self.assertEqual(EXPECTED_XML_PATH, self.source.getSourcePath())

    def testGetSourceType(self) -> None:
        EXPECTED_TYPE = "XML file"
        self.assertEqual(EXPECTED_TYPE, self.source.getSourceType())

    def testNormaliseDataToItems(self) -> None:
        EXPECTED_ITEMS = [
            Item(
                model="xmltestmodel1",
                stock_level=3,
                attributes={
                    "productName": "XML test model name 1 normal stock"
                },
            ),
            Item(
                model="xmltestmodel2",
                stock_level=0,
                attributes={
                    "productName": "XML test model name 2 out of stock"
                },
            ),
            Item(
                model="xmltestmodel3",
                stock_level=999999,
                attributes={
                    "productName": "XML test model name 3 lots of stock"
                },
            ),
        ]
        item_list = self.source.normaliseDataToItems()
        for index, item in enumerate(item_list):
            self.assertTrue(item == EXPECTED_ITEMS[index])
