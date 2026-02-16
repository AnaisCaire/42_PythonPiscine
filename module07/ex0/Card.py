
from abc import ABC, abstractmethod


class Card(ABC):
    """The abstract foundation class"""
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Base implementation for playing a card.
        Subclasses should call super().play(game_state) to include
        this basic information.
        """
        # we do not overwite the class each time
        # but we update it to be like a historic
        game_state.update({
            "card_played": self.name,
            "mana_used": self.cost,
            "rarity": self.rarity
        })
        return game_state

    def get_card_info(self) -> dict:
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        })

    def is_playable(self, available_mana: int) -> bool:
        """Checks if there is more than 5 mana to be playable"""
        return available_mana >= self.cost
