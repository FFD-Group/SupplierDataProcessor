import unittest
from Sources import Item
from faker import Faker


def _generateTestItem(**overrides: dict) -> Item.Item:
    """Generate a test Item optionally with the given overrides.
    @param overrides: dict - an optional dictionary of values to use in the Item properties.
    @return an Item instance"""
    fake = Faker()
    stock_status_values = ["In Stock", "Out of Stock"]
    attribute_dict = dict()
    for _ in range(fake.random_digit()):
        attribute_dict[f"{fake.word()}"] = f"{fake.word()}"
    return Item.Item(
        model=overrides.get("model", fake.word()),
        stock_status=overrides.get(
            "stock_status",
            fake.pyint(min_value=0, max_value=len(stock_status_values)),
        ),
        stock_level=overrides.get("stock_level", fake.random_number(fix_len=2)),
        rrp=overrides.get(
            "rrp",
            fake.pydecimal(positive=True, min_value=0.01, max_value=99_999.00),
        ),
        cost=overrides.get(
            "cost",
            fake.pydecimal(positive=True, min_value=0.01, max_value=99_999.00),
        ),
        attributes=overrides.get("attributes", attribute_dict),
    )


class testItem(unittest.TestCase):
    """Tests for the Item class."""

    @classmethod
    def setUpClass(self) -> None:
        self.faker = Faker()

    def setUp(self) -> None:
        self.testItem1 = _generateTestItem(
            overrides={
                "attributes": {
                    "tangerine": "orange",
                    "banana": "yellow",
                    "kiwi": "brown",
                }
            }
        )
        self.testItemOne = self.testItem1
        self.testItem2 = _generateTestItem(overrides={"model": "testItem2"})

    def test_eq(self) -> None:
        self.assertFalse(self.testItem1 == self.testItem2)
        self.assertTrue(self.testItem1 == self.testItemOne)
        with self.assertRaises(NotImplementedError):
            self.testItem1 == "banana"


if __name__ == "__main__":
    unittest.main()
