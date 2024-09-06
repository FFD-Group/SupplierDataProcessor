from pprint import pprint
import unittest
from Sources.Normaliser import Normaliser
from Sources.tests.testItem import _generateTestItem


class testNormaliser(unittest.TestCase):
    """Testing the Item model."""

    def testNormalise(self) -> None:
        """Ensure the normaliser can handle different types of
        input and output a uniform result which can be
        represented as Items"""
        normaliser = Normaliser()
        input_test_data_1 = [
            '{"sku":"testModel","price":100.00,"availability":"In Stock"'
            + ',"qty":435,"cost":75.00,"tangerine":"orange",'
            + '"banana":"yellow","kiwi":"brown"}',
        ]
        correct_output_item_1 = _generateTestItem(
            overrides={
                "model": "testModel",
                "stock_status": "In Stock",
                "stock_level": 435,
                "rrp": 100.00,
                "cost": 75.00,
                "attributes": {
                    "tangerine": "orange",
                    "banana": "yellow",
                    "kiwi": "brown",
                },
            }
        )

        output_data_1 = normaliser.normalise(input_test_data_1)
        self.assertEqual(output_data_1[0], correct_output_item_1)


if __name__ == "__main__":
    unittest.main()
