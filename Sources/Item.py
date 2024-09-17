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

    @property
    def model_attrs(self) -> List[str]:
        return ["model", "stock_status", "stock_level", "rrp", "cost"]

    def __init__(
        self,
        model: str,
        stock_status: str,
        stock_level: int,
        rrp: Decimal,
        cost: Decimal,
        **attributes,
    ) -> None:
        """Initialise an Item instance with the given properties.

        Keyword arguments:

        @model -- the model number of the Item.
        @stock_status -- the availability of the Item.
        @stock_level -- a number representing the quantity available.
        @rrp -- Recommended Retail Price.
        @cost -- how much the Item costs.
        @attributes -- a dictionary of attribute labels & values.
        """
        try:
            self.model = str(model)
            self.stock_status = str(stock_status)
            self.stock_level = int(stock_level)
            self.rrp = Decimal(rrp)
            self.cost = Decimal(cost)
        except ValueError as value_exception:
            raise value_exception
        self.attributes = []
        self.attributes.append((label, value) for (label, value) in attributes)

    def __eq__(self, other) -> bool:
        """Equality operator overload for comparing the equality of
        two Item instances.

        #### Keyword arguments:

        @other -- the other instance to compare this Item to.

        #### Returns:

        A bool signifying equality of the compared Items.

        #### Raises:

        NotImplementedError -- if other is not an instance of Item.
        """
        if not isinstance(other, Item):
            raise NotImplementedError
        for attr in self.model_attrs:
            if not getattr(other, attr):
                return False
            other_value = getattr(other, attr)
            self_value = getattr(self, attr)
            if getattr(other, attr) != getattr(self, attr):
                return False
        return True

    def __repr__(self) -> str:
        """Representation of Item."""
        return f"{self.model} - {self.stock_status} ({self.stock_level} available) - £{self.rrp} RRP, £{self.cost} cost"

    def __str__(self) -> str:
        """String representation of Item."""
        return (
            f"Item model: {self.model}"
            + f" with a list price of {self.rrp}, a cost of {self.cost}, "
            + f"is {self.stock_status} with {self.stock_level} available."
        )
