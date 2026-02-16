from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """The simple orchestrator for DataDeck simulations."""

    def __init__(self):
        """Initialize the engine with empty components."""
        self._factory = None
        self._strategy = None

    def configure_engine(self,
                         factory: CardFactory, strategy: GameStrategy) -> None:
        """Link the factory and strategy to the engine."""
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        """Execute a turn using the current strategy and factory."""
        if not self._strategy or not self._factory:
            raise RuntimeError("Engine must be configured before simulation.")

        # 1. Use the factory to generate a small hand
        deck_data = self._factory.create_themed_deck(3)
        hand = deck_data.get("cards", [])

        # 2. Use the strategy to process the turn
        # We pass an empty list for the battlefield to keep it simple
        return self._strategy.execute_turn(hand, [])

    def get_engine_status(self) -> dict:
        """Return the current state of the engine configuration."""
        return {
            "factory_name":
            type(self._factory).__name__ if self._factory else None,
            "strategy_name":
            self._strategy.get_strategy_name() if self._strategy else None
        }
