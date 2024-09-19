from typing import List
from Sources.Item import Item
from Sources.Source import Source
import logging

logger = logging.getLogger(__name__)


class SourcesOrchestrator:

    sources: List[Source]
    item_list: List[Item]

    def __init__(self) -> None:
        self.sources = []
        self.item_list = []

    def addSource(self, source: Source) -> None:
        if not isinstance(source, Source):
            raise ValueError
        if source not in self.sources:
            self.sources.append(source)

    def removeSource(self, source: Source) -> None:
        if not isinstance(source, Source):
            raise ValueError
        if source in self.sources:
            self.sources.remove(source)

    def readItems(self) -> List[Item]:
        self.item_list.clear()
        for source in self.sources:
            try:
                self.item_list.extend(source.normaliseDataToItems())
            except Exception as exception:
                logger.exception(exception)
                continue
        return self.item_list
