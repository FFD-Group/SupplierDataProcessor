from decimal import Decimal
from typing import List

MIN_STOCK_THRESHOLD = 0
AVAILABILITY_VALUE_SYMONYMS = ["Yes", "In Stock", "Low Stock"]


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
        model: str = None,
        stock_status: str = None,
        stock_level: int = 0,
        rrp: Decimal = 0.00,
        cost: Decimal = 0.00,
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
            self.model = str(model) if model else None
            self.stock_level = int(stock_level) if stock_level else int(0)
            self.stock_status = self._deriveStockStatus(
                stock_status, stock_level
            )
            self.rrp = Decimal(rrp) if rrp else Decimal(0.00)
            self.cost = Decimal(cost) if cost else Decimal(0.00)
        except ValueError as value_exception:
            raise value_exception
        self.attributes = []
        self.attributes.append((label, value) for (label, value) in attributes)

    def _deriveStockStatus(self, status: str = None, level: int = None) -> str:
        """Favour the status that is provided by the source primarily. If the status
        is not explicitly supplied, fallback on the level given otherwise return
        that the Item is unavailable."""
        if status and status in AVAILABILITY_VALUE_SYMONYMS:
            return "In Stock"
        if not status:
            if int(level) > MIN_STOCK_THRESHOLD:
                return "In Stock"
        return "Out of Stock"

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
            if not hasattr(other, attr):
                return False
            other_value = getattr(other, attr)
            self_value = getattr(self, attr)
            if getattr(other, attr) != getattr(self, attr):
                return False
        return True

    def __repr__(self) -> str:
        """Representation of Item."""
        return self.__str__()

    def __str__(self) -> str:
        """String representation of Item."""
        model = self.model or "<None>"
        rrp = self.rrp or 0.00
        cost = self.cost or 0.00
        stock_status = self.stock_status or "<Unknown>"
        stock_level = (
            self.stock_level if self.stock_level is not None else "<Unknown>"
        )
        return (
            f"Item model: {model}"
            + f" with a list price of {rrp}, a cost of {cost}, "
            + f"is {stock_status} with {stock_level} available."
        )
