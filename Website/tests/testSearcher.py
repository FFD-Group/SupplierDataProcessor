import json
import unittest
from unittest.mock import patch, MagicMock
from Website.Product import Product
from Website.Searcher import Searcher


class TestSearcher(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.searcher = Searcher()
        self.existing_sku = "testmodel1"
        self.non_existant_sku = "testmodel0"
        self.manufacturers = ["ACME", "FFD"]
        with open("files/test_website_product.json") as product_json_file:
            self.api_product_json = json.loads(product_json_file.read())
        with open("files/test_website_no_product.json") as no_product_json_file:
            self.api_no_product_json = json.loads(no_product_json_file.read())

    @patch("Searcher.requests.get")
    def testSearchForProductExists(self, mock_requests) -> None:
        # Assert product found when exists
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = (
            self.api_product_json
        )  # calling response.json() in method will return this
        mock_requests.get.return_value = mock_response
        expected_product = Product()
        self.assertEqual(
            self.searcher.searchForProduct(
                self.existing_sku, self.manufacturers[0]
            ),
            expected_product,
        )

    @patch("Searcher.requests.get")
    def testSearchForProductDoesNotExist(self, mock_requests) -> None:
        # Assert product not found when doesn't exist
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.api_no_product_json
        mock_requests.get.return_value = mock_response
        self.assertIsNone(
            self.searcher.searchForProduct(
                self.non_existant_sku, self.manufacturers[0]
            )
        )

    @patch("Searcher.requests.get")
    def testSearchForProductDoesNotExistForManufacturer(
        self, mock_requests
    ) -> None:
        # Assert product not found when exists but different manufacturer
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.api_no_product_json
        mock_requests.get.return_value = mock_response
        self.assertIsNone(
            self.searcher.searchForProduct(
                self.existing_sku, self.manufacturers[1]
            )
        )

    @patch("Searcher.requests.get")
    def testSearchForProductConnectionError(self, mock_requests) -> None:
        # Assert exception when web unavailable
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_requests.get.return_value = mock_response
        with self.assertRaises(ConnectionError):
            self.searcher.searchForProduct(
                self.existing_sku, self.manufacturers[0]
            )
