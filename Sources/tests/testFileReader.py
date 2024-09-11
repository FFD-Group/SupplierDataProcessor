import json
import unittest

from Sources.XMLFile import XMLFile, XMLReader
from Sources.Spreadsheet import Spreadsheet, SpreadsheetReader

TEST_XML_CORRECT_OUTCOME = [
    '{"productCode":"xmltestmodel1","productName":"XML test model name 1 normal stock","stockLevel":"3"}',
    '{"productCode":"xmltestmodel2","productName":"XML test model name 2 out of stock","stockLevel":"0"}',
    '{"productCode":"xmltestmodel3","productName":"XML test model name 3 lots of stock","stockLevel":"999999"}',
]
TEST_CSV_CORRECT_OUTCOME = [
    '{"SKU":"csvtestmodel1","Manufacturer":"CSVACME","Product Name":"CSVACME test model 1 with low stock","Description":"<p>Here is a great product description with lots of lovely words.</p><p>Here is an unordered list:</p><ul><li>Attribute 1 is great</li><li>I really like this colour</li><li>This point has an \' in it</li><li>This one has a \“ in it</li></ul><p>What a great description.</li>","List Price":"4198","Availability":"Low Stock","GTIN":"1111111111111","Manufacturer Warranty":"1 Year Parts Only","Energy Rating":"A","Dimensions (mm)":"W500 x D367 x H1234","Height (mm)":"1234","Width (mm)":"500","URL":"https://www.ffdgroup.co.uk/fakeurl","Product Image":"https://www.ffdgroup.co.uk/media/fakeimage.jpg"}',
    '{"SKU":"csvtestmodel2","Manufacturer":"CSVACME","Product Name":"CSVACME test model 2 with normal stock","Description":"<p>Here is a great product description with lots of lovely words.</p><p>Here is an unordered list:</p><ul><li>Attribute 1 is great</li><li>I really like this colour</li><li>This point has an \' in it</li><li>This one has a \“ in it</li></ul><p>What a great description.</li>","List Price":"4250","Availability":"In Stock","GTIN":"1111111111122","Manufacturer Warranty":"1 Year Parts and Labour","Energy Rating":"B","Dimensions (mm)":"W0.3 x D111 x H0001","Height (mm)":"1","Width (mm)":"0.3","URL":"https://www.ffdgroup.co.uk/fakeurl","Product Image":"https://www.ffdgroup.co.uk/media/fakeimage.jpg"}',
    '{"SKU":"aroguecsvmodel","Manufacturer":"rogueCSVmanufacturer","Product Name":"Some rogue name in the CSV file","Description":"<p>Here is a great product description with lots of lovely words.</p><p>Here is an unordered list:</p><ul><li>Attribute 1 is great</li><li>I really like this colour</li><li>This point has an \' in it</li><li>This one has a \“ in it</li></ul><p>What a great description.</li>","List Price":"1598","Availability":"In Stock","GTIN":"1111111111133","Manufacturer Warranty":"12 Months B2B","Energy Rating":"C","Dimensions (mm)":"W2345 x D9 x H23","Height (mm)":"23","Width (mm)":"2345","URL":"https://www.ffdgroup.co.uk/fakeurl","Product Image":"https://www.ffdgroup.co.uk/media/fakeimage.jpg"}',
    '{"SKU":"csvtestmodel3","Manufacturer":"CSVACME","Product Name":"CSVACME test model 3 with No stock","Description":"<p>Here is a great product description with lots of lovely words.</p><p>Here is an unordered list:</p><ul><li>Attribute 1 is great</li><li>I really like this colour</li><li>This point has an \' in it</li><li>This one has a \“ in it</li></ul><p>What a great description.</li>","List Price":"1598","Availability":"Out of Stock","GTIN":"1111111111144","Manufacturer Warranty":"1 Year Parts Only","Energy Rating":"D","Dimensions (mm)":"W2345 x D464 x H235","Height (mm)":"235","Width (mm)":"2345","URL":"https://www.ffdgroup.co.uk/fakeurl","Product Image":"https://www.ffdgroup.co.uk/media/fakeimage.jpg"}',
]


class TestFileReader(unittest.TestCase):

    def setUp(self) -> None:
        self.test_xml_file = XMLFile(
            "files/test_xml_file.xml", XMLReader("product")
        )
        self.test_csv_file = Spreadsheet(
            "files/test_spreadsheet.csv", SpreadsheetReader
        )

    def testReadFile(self) -> None:
        xml_file_read_result = self.test_xml_file.readFile()
        for index, xml_item_as_json in enumerate(xml_file_read_result):
            xml_item = json.loads(xml_item_as_json)
            expected = json.loads(TEST_XML_CORRECT_OUTCOME[index])
            for key in expected:
                self.assertTrue(key in xml_item)
                self.assertEqual(expected[key], xml_item[key])
        csv_file_read_result = self.test_csv_file.readFile()
        for index, csv_item_as_json in enumerate(csv_file_read_result):
            csv_item = json.loads(csv_item_as_json)
            expected = json.loads(TEST_CSV_CORRECT_OUTCOME[index])
            for key in expected:
                self.assertTrue(key in csv_item)
                self.assertEqual(expected[key], csv_item[key])
