import unittest

from Item import Item


class TestItem(unittest.TestCase):
    """Tests for the Item class."""

    def setUp(self) -> None:
        self.testItem1 = Item(
            "testItem1",
            "In stock",
            54,
            100.00,
            75.00,
            {"tangerine": "orange", "banana": "yellow", "kiwi": "brown"},
        )
        self.testItemOne = Item(
            "testItem1",
            "In stock",
            54,
            100.00,
            75.00,
            {"tangerine": "orange", "banana": "yellow", "kiwi": "brown"},
        )
        self.testItem2 = Item(
            "testItem2",
            "Out of Stock",
            0,
            350.00,
            245.00,
            {"width": "456", "finish": "Stainless steel"},
        )

    def test_eq(self) -> None:
        self.assertFalse(self.testItem1 == self.testItem2)
        self.assertTrue(self.testItem1 == self.testItemOne)
        self.assertRaises(NotImplemented, (self.testItem1 == "banana"))


if __name__ == "__main__":
    unittest.main()
