from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Combat interface, assuring every combatable
    card has these 3 methods
    """

    @abstractmethod
    def attack(self, target: str) -> dict:
        """ attack """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """ Damage """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """ Dictionary of stats """
        pass
