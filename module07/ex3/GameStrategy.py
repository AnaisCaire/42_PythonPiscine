from abc import ABC, abstractmethod

class GameStrategy(ABC):
    """ The game strategy skeleton """

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """ make a turn """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """ get the name """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """ prioritize targets """
        pass