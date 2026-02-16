
from ex0.Card import Card


class CreatureCard(Card):
    """Gives play and attack based on the Parent class Card"""
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not (isinstance(attack, int) and attack > 0):
            raise ValueError("The attack is not valid")
        if not (isinstance(health, int) and health > 0):
            raise ValueError("The health is not valid")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """prints the play results"""
        game_state = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature suummond to battlefield"
                }
        return game_state

    def attack_target(self, target) -> dict:
        """Gives attack info and validation of health and attack points"""
        message = {
                "attacker": self.name,
                "target": target,
                "damage_dealt": self.attack,
                "combat_resolved": True
            }
        return message
