from typing import List
from Sources.Item import Item
from Sources.Normaliser import Normaliser
from Sources.SourceProtocol import SourceProtocol


class Source:
    """The Source class is responsible for orchestrating source reading,
    normalising and holding a reference to the read list of items.
    """

    item_list: List[Item]
    normaliser: Normaliser
    source: SourceProtocol

    def __init__(self, source: SourceProtocol) -> None:
        self.normaliser = Normaliser()
        self.source = source
        self.item_list = []

    def getSourcePath(self) -> str | None:
        """Return the source's path (if it has one)."""
        return self.source.getSourcePath()

    def getSourceType(self) -> str:
        """Return the source's type."""
        return self.source.getSourceType()

    def normaliseDataToItems(self) -> List[Item]:
        """Return a normalised list of Items from the
        source data."""
        data = self.source.readSource()
        self.item_list = self.normaliser.normalise(data)
        return self.item_list
