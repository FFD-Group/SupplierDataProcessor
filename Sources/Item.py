from decimal import Decimal
from typing import List


class Item:
    """The Item class is a model of the source data representing a product."""

    model: str
    stock_status: str
    stock_level: int
    rrp: Decimal
    cost: Decimal
    attributes: List[tuple]

    def __init__(
        self,
        model: str,
        stock_status: str,
        stock_level: int,
        rrp: Decimal,
        cost: Decimal,
        **attributes,
    ) -> None:
        """Initialise an Item instance with the given properties."""
        self.model = model
        self.stock_status = stock_status
        self.stock_level = stock_level
        self.rrp = rrp
        self.cost = cost
        self.attributes = []
        self.attributes.append((label, value) for (label, value) in attributes)

    def __eq__(self, other) -> bool:
        """Equality operator overload for comparing the equality of
        two Item instances."""
        if not isinstance(other, Item):
            raise NotImplementedError
        for attr in vars(self):
            if not getattr(other, attr):
                print(f"{attr} on this Item is not the same as other Item")
                return False
            if getattr(other, attr) != getattr(self, attr):
                return False
        return True
