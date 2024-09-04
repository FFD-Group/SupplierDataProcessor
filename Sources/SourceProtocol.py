from typing import List, Protocol


class SourceProtocol(Protocol):
    """Provides a way to read items from an identifiable source."""

    def getSourcePath(self) -> str:
        """Get the path of a source if it has one."""
        raise NotImplementedError

    def getSourceType(self) -> str:
        """Return the type of the source."""
        raise NotImplementedError

    def readSource(self) -> List[str]:
        """Read and return the read items from the source."""
        raise NotImplementedError
