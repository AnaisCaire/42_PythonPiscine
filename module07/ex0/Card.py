
from abc import ABC, abstractmethod


class Card(ABC):
    """The abstract foundation class"""
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Give the play results"""
        pass

    def get_card_info(self) -> dict:
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        })

    def is_playable(self, available_mana: int) -> bool:
        """Checks if there is more than 5 mana to be playable"""
        return available_mana >= self.cost
