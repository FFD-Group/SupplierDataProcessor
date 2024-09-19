import json
from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional
from Sources.Item import Item
from dataclass_wizard import json_field, JSONSerializable
from dataclass_wizard.errors import UnknownJSONKey

MODEL_FIELD_NAMES = [
    "sku",
    "product",
    "model_number",
    "productCode",
    "SKU",
    "Item Code",
]
STOCK_STATUS_FIELD_NAMES = ["availability", "Availability", "Stock Avail."]
STOCK_LEVEL_FIELD_NAMES = ["qty", "quantity", "stock level"]
COST_FIELD_NAMES = ["cost"]
RRP_FIELD_NAMES = ["rrp", "price", "List Price", "List Price GBP"]


@dataclass
class DataItem(JSONSerializable):
    """Intermediary dataclass for Items to allow for normalisation
    with varying data source keys."""

    # Need a way to get these mapping lists of strings from a user-definable
    # source so that the maintainer doesn't have to keep up with changes
    # in sources.
    model: Optional[str] = json_field(MODEL_FIELD_NAMES, all=True, default="")
    stock_status: Optional[str] = json_field(
        STOCK_STATUS_FIELD_NAMES, all=True, default=""
    )
    stock_level: Optional[str] = json_field(
        STOCK_LEVEL_FIELD_NAMES, all=True, default=0
    )
    cost: Optional[Decimal] = json_field(
        COST_FIELD_NAMES, all=True, default=0.0
    )
    rrp: Optional[Decimal] = json_field(RRP_FIELD_NAMES, all=True, default=0.0)
    attributes: dict = None

    def convertToItem(self) -> Item:
        """Convert the DataItem to a regular Item instance.

        Returns:

        The Item instance with the same properties as this DataItem.
        """
        return Item(
            model=self.model,
            stock_status=self.stock_status,
            stock_level=self.stock_level,
            rrp=self.rrp,
            cost=self.cost,
            attributes=self.attributes,
        )


class Normaliser:
    """The Normaliser class will normalise json data read from a source in
    order to make sure it can be represented as a list of Items."""

    def normalise(self, data: List[str]) -> List[Item]:
        normalised_items = []
        for source_item in data:
            try:
                data_item = DataItem.from_dict(json.loads(source_item))
                normalised_items.append(data_item.convertToItem())
            except UnknownJSONKey as unknown_key_exception:
                raise unknown_key_exception
        return normalised_items
