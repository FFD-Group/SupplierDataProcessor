import unittest
from Normaliser import Normaliser
from Item import Item


class TestNormaliser(unittest.TestCase):
    """Testing the Item model."""

    def test_normalise(self) -> None:
        """Ensure the normaliser can handle different types of
        input and output a uniform result which can be
        represented as Items"""
        normaliser = Normaliser()
        input_test_data_1 = [
            "sku,price,availability,qty,cost,tangerine,banana,kiwi\n",
            "testModel,100.00,in stock,435,75,orange,yellow,brown",
        ]
        correct_output_item_1 = Item()
        correct_output_item_1.model = "testModel"
        correct_output_item_1.stock_status = "In Stock"
        correct_output_item_1.stock_level = 435
        correct_output_item_1.rrp = 100.00
        correct_output_item_1.cost = 75.00
        correct_output_item_1.attributes = [
            ("tangerine", "orange"),
            ("banana", "yellow"),
            ("kiwi", "brown"),
        ]

        output_data_1 = normaliser.normalise(input_test_data_1)
        self.assertEqual(output_data_1, correct_output_item_1)


if __name__ == "__main__":
    unittest.main()
