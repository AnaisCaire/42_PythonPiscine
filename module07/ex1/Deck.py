import random
from typing import List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck():
    """Deck management system for handling various card types."""
    def __init__(self) -> None:
        """Initialize an empty deck."""
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck"""
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck"""
        for cards in self._cards:
            if cards.name == card_name:
                self._cards.remove(cards)
                return True
        return False

    def shuffle(self) -> None:
        """Randomize the order of cards in the deck."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Remove and return the top card from the deck."""
        if not self._cards:
            raise IndexError("Cannot draw from an empty deck")
        return self._cards.pop()

    def get_deck_stats(self) -> dict:
        """Calculate and return statistics about the current deck."""
        stats = {
            "total_cards": len(self._cards),
            "creatures":
            sum(1 for c in self._cards if isinstance(c, CreatureCard)),
            "spells":
            sum(1 for c in self._cards if isinstance(c, SpellCard)),
            "artifacts":
            sum(1 for c in self._cards if isinstance(c, ArtifactCard)),
            "avg_cost":
            sum(c.cost for c in self._cards) / len(self._cards)
            if self._cards else 0.0
        }
        return stats
