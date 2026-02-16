from abc import ABC, abstractmethod


class Rankable(ABC):
    """Simple ranking interface."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return current rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update wins count."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update losses count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return ranking info as a dict."""
        pass
