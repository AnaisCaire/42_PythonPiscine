
from abc import ABC, abstractmethod


class Magical(ABC):
    """ MAgical structre for cards"""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """ Spell casting """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """ Mana channeled in Mana amout """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """ dict of stats """
        pass
