import unittest
from Sources.Item import Item
from Sources.Source import Source
from Sources.XMLFile import XMLFile, XMLReader
from Sources.Spreadsheet import Spreadsheet, SpreadsheetReader
from Sources.SourcesOrchestrator import SourcesOrchestrator

TEST_XML_FILE_PATH = "files/test_xml_file.xml"
TEST_XML_FILE_PATH_2 = "files/test_xml_file_2.xml"
TEST_CSV_FILE_PATH = "files/test_spreadsheet.csv"
TEST_XLSX_FILE_PATH = "files/test_spreadsheet.xlsx"


class testSourcesOrchestrator(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.sourceOrchestrator = SourcesOrchestrator()
        xml_reader = XMLReader()
        xml_file = XMLFile(TEST_XML_FILE_PATH, xml_reader)
        xml_source = Source(xml_file)
        spreadsheet_reader = SpreadsheetReader()
        spreadsheet_csv_file = Spreadsheet(
            TEST_CSV_FILE_PATH, spreadsheet_reader
        )
        spreadsheet_csv_source = Source(spreadsheet_csv_file)
        spreadsheet_xlsx_file = Spreadsheet(
            TEST_XLSX_FILE_PATH, spreadsheet_reader, 3
        )
        spreadsheet_xlsx_source = Source(spreadsheet_xlsx_file)
        self.sourceOrchestrator.sources.append(xml_source)
        self.sourceOrchestrator.sources.append(spreadsheet_csv_source)
        self.sourceOrchestrator.sources.append(spreadsheet_xlsx_source)

    def testAddSource(self) -> None:
        xml_reader = XMLReader()
        xml_file = XMLFile(TEST_XML_FILE_PATH, xml_reader)
        xml_source = Source(xml_file)
        # Assert sources are added
        self.assertFalse(xml_source in self.sourceOrchestrator.sources)
        self.sourceOrchestrator.addSource(xml_source)
        self.assertTrue(xml_source in self.sourceOrchestrator.sources)
        # Assert non-sources can't be added
        with self.assertRaises(ValueError):
            self.sourceOrchestrator.addSource(xml_reader)
        # Assert the same source can't be added twice
        source_count = len(self.sourceOrchestrator.sources)
        self.sourceOrchestrator.addSource(xml_source)
        self.assertEqual(source_count, len(self.sourceOrchestrator.sources))

    def testRemoveSource(self) -> None:
        xml_reader = XMLReader()
        xml_file = XMLFile(TEST_XML_FILE_PATH_2, xml_reader)
        xml_source = Source(xml_file)
        self.sourceOrchestrator.removeSource(xml_source)
        self.assertFalse(xml_source in self.sourceOrchestrator.sources)
        # Assert source not in sources doesn't throw error
        self.sourceOrchestrator.removeSource(xml_source)
        # Assert non-source raises error
        with self.assertRaises(ValueError):
            self.sourceOrchestrator.removeSource(xml_reader)

    def testReadItems(self) -> None:
        self.assertFalse(len(self.sourceOrchestrator.item_list) > 0)
        items = self.sourceOrchestrator.readItems()
        self.assertTrue(len(self.sourceOrchestrator.item_list) > 0)
        # Assert item list is all instances of Item
        for item in items:
            self.assertTrue(isinstance(item, Item))
        # Assert item list empty with no sources
        self.sourceOrchestrator.sources.clear()
        items = self.sourceOrchestrator.readItems()
        self.assertTrue(len(items) == 0)
