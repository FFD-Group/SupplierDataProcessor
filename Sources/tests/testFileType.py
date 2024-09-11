import unittest

from Sources import XMLFile
from Sources import Spreadsheet

# XMLFile
TEST_XML_FILE_PATH = "files/test_xml_file.xml"
# Spreadsheet
TEST_SPREADSHEET_XLSX_PATH = "files/test_spreadsheet.xlsx"
TEST_SPREADSHEET_CSV_PATH = "files/test_spreadsheet.csv"
XLSX_SPREADSHEET_FILE_TYPE = Spreadsheet.SPREADSHEET_FILE_TYPE.format("XLSX")
CSV_SPREADSHEET_FILE_TYPE = Spreadsheet.SPREADSHEET_FILE_TYPE.format("CSV")


class TestFileType(unittest.TestCase):

    def setUp(self) -> None:
        """Create some test files."""
        self.test_xml_file = XMLFile.XMLFile(
            TEST_XML_FILE_PATH, XMLFile.XMLReader
        )
        self.test_spreadsheet_xlsx = Spreadsheet.Spreadsheet(
            TEST_SPREADSHEET_XLSX_PATH, Spreadsheet.SpreadsheetReader
        )
        self.test_spreadsheet_csv = Spreadsheet.Spreadsheet(
            TEST_SPREADSHEET_CSV_PATH, Spreadsheet.SpreadsheetReader
        )

    def testCreateFileType(self) -> None:
        """Test the creation of FileTypes."""
        with self.assertRaises(FileNotFoundError):
            _ = XMLFile.XMLFile("path/does/not/exist.xml", XMLFile.XMLReader)
        with self.assertRaises(FileNotFoundError):
            _ = Spreadsheet.Spreadsheet(
                "path/does/not/exist.csv", Spreadsheet.SpreadsheetReader
            )

    def testGetFilePath(self) -> None:
        """Test the FileType's file path is returned correctly."""
        self.assertEqual(self.test_xml_file.getFilePath(), TEST_XML_FILE_PATH)
        self.assertEqual(
            self.test_spreadsheet_xlsx.getFilePath(), TEST_SPREADSHEET_XLSX_PATH
        )
        self.assertEqual(
            self.test_spreadsheet_csv.getFilePath(), TEST_SPREADSHEET_CSV_PATH
        )

    def testGetFileType(self) -> None:
        """Test the FileType's type is returned correctly."""
        self.assertEqual(
            self.test_xml_file.getFileType(), XMLFile.XML_FILE_TYPE
        )
        self.assertEqual(
            self.test_spreadsheet_xlsx.getFileType(),
            XLSX_SPREADSHEET_FILE_TYPE,
        )
        self.assertEqual(
            self.test_spreadsheet_csv.getFileType(),
            CSV_SPREADSHEET_FILE_TYPE,
        )
