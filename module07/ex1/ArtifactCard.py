from ex0.Card import Card

class ArtifactCard(Card):
    """Concrete implementation for permanent game modifiers."""

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        """Initialize ArtifactCard with durability and permanent effect."""
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer.")  
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Process the playing of the artifact."""
        game_state = {"card_played": self.name,
                    "mana_used": self.cost,
                   "effect": f"Permanent: {self.effect}"}
        return game_state

    def activate_ability(self) -> dict:
        """Activate the ongoing effect of the artifact."""
        return {
            "artifact": self.name,
            "action": "Ability activated",
            "effect_description": self.effect,
            "remaining_durability": self.durability}