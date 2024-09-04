from typing import List
from Sources.Item import Item


class Normaliser:
    """The Normaliser class will normalise data read from a source in
    order to make sure it can be represented as a list of Items."""

    def normalise(self, data: List[str]) -> List[Item]:
        raise NotImplementedError
