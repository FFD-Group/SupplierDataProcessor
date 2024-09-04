from typing import List
from Item import Item
from Sources import Normaliser, SourceProtocol


class Source:
    """The Source class is responsible for orchestrating source reading,
    normalising and holding a reference to the read list of items.
    """

    item_list: List[Item]
    normaliser: Normaliser
    source: SourceProtocol

    def getSourcePath(self) -> str | None:
        """Return the source's path (if it has one)."""
        return self.source.getSourcePath()

    def getSourceType(self) -> str:
        """Return the source's type."""
        return self.source.getSourceType()

    def normaliseDataToItems(self, data: List[str]) -> List[Item]:
        """Return a normalised list of Items from the
        source data."""
        self.item_list = self.normaliser.normalise(data)
        return self.item_list
