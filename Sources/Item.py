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
        """Initialise an Item instance with the given properties.

        Keyword arguments:

        @model -- the model number of the Item.
        @stock_status -- the availability of the Item.
        @stock_level -- a number representing the quantity available.
        @rrp -- Recommended Retail Price.
        @cost -- how much the Item costs.
        @attributes -- a dictionary of attribute labels & values.
        """
        self.model = model
        self.stock_status = stock_status
        self.stock_level = stock_level
        self.rrp = rrp
        self.cost = cost
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
        for attr in vars(self):
            if not getattr(other, attr):
                print(f"{attr} on this Item is not the same as other Item")
                return False
            if getattr(other, attr) != getattr(self, attr):
                return False
        return True
