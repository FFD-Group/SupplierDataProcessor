from dataclasses import dataclass
from decimal import Decimal
import json
from typing import List
from Sources.Item import Item
from dataclass_wizard import json_field, JSONSerializable
from dataclass_wizard.errors import UnknownJSONKey


@dataclass
class DataItem(JSONSerializable):
    """Intermediary dataclass for Items to allow for normalisation
    with varying data source keys."""

    # Need a way to get these mapping lists of strings from a user-definable
    # source so that the maintainer doesn't have to keep up with changes
    # in sources.
    model: str = json_field(("sku", "product", "model_number"), all=True)
    stock_status: str = json_field("availability", all=True)
    stock_level: str = json_field(("qty", "quantity", "stock level"), all=True)
    cost: Decimal = json_field("cost", all=True)
    rrp: Decimal = json_field(("rrp", "price"), all=True)
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
    """The Normaliser class will normalise data read from a source in
    order to make sure it can be represented as a list of Items."""

    def normalise(self, data: List[str]) -> List[Item]:
        normalised_items = []
        for source_item in data:
            try:
                data_item = DataItem.from_dict(json.loads(source_item))
                normalised_items.append(data_item.convertToItem())
            except UnknownJSONKey as unknown_key:
                print(unknown_key)
        return normalised_items
