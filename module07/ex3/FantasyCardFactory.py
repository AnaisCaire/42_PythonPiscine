from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """Concrete factory for creating Fantasy-themed cards."""

    def create_creature(self, name_or_power: str) -> CreatureCard:
        """Create fantasy creatures """
        if name_or_power.lower() == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        if name_or_power.lower() == "goblin warrior":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        raise ValueError("there is no creature like this")

    def create_spell(self, name_or_power: str) -> SpellCard:
        """Create elemental spells"""
        if name_or_power.lower() == "fire":
            return SpellCard("Fireball", 3, "Rare", "damage")
        if name_or_power.lower() == "ice":
            return SpellCard("Ice Blast", 2, "Common", "debuff")
        raise ValueError("this is not a spell")

    def create_artifact(self, name_or_power: str) -> ArtifactCard:
        """Create magical artifacts """
        if name_or_power.lower() == "ring":
            return ArtifactCard("Mana Ring", 2, "Rare", 3, "Gain mana")
        if name_or_power.lower() == "staff":
            return ArtifactCard("Wizard Staff", 4, "Epic", 2, "Boost spells")
        raise ValueError("this is not an artifact")

    def create_themed_deck(self, size: int) -> dict:
        """Make a dictionary with a themed deck"""
        cards = []
        for i in range(size):
            # Logic to populate the deck with a mix of types
            cards.append(self.create_creature("goblin warrior"))
        return {
            "theme": "Fantasy",
            "size": len(cards),
            "cards": cards
        }

    def get_supported_types(self) -> dict:
        """Return the available types for this factory"""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fire", "ice"],
            "artifacts": ["ring", "staff"]
        }
