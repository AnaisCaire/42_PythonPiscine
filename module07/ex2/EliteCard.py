from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """ Implements all 3 abstract classes"""
    def __init__(self, name: str,
                 cost: int, rarity: str, damage_done: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.damage_done = damage_done
        self.health = health

    def play(self, game_state: dict) -> dict:
        """from the card class abstract method"""
        game_state = super().play(game_state)
        game_state.update({"state": "Elite card entered the field"})
        return game_state

    # combatable methods:
    def attack(self, target: str) -> dict:
        """ Who attacked who and how much ? """
        if self.damage_done <= 5:
            combat_type = "meele"
        else:
            combat_type = "Magic sword"
        return {"attacker": self.name,
                "target": target,
                "damage": self.damage_done,
                "combat_type": combat_type}

    def defend(self, incoming_damage: int) -> dict:
        """
        Who is the defender, how much damage has he taken
        how much damage did he block and is he still alive?
        """
        self.health -= incoming_damage
        if self.health >= 0:
            alive = True
        else:
            alive = False
        return {"defender": self.name,
                "damage_taken": incoming_damage,
                "damage_blocked": self.damage_done - 2,
                "still_alive": alive
                }

    # magical methods:
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """What spell was cast by who ? to who?"""
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost - 6
        }

    def channel_mana(self, amount: int) -> dict:
        """
        How much of mana was channeled and how
        much do you have now.
        """
        total_mana = self.cost - amount
        return {
            "channeled": amount,
            "total_mana": total_mana}

    # Implement stats methods
    def get_combat_stats(self) -> dict:
        """Return combat stats."""
        return {"attack": self.attack, "health": self.health}

    def get_magic_stats(self) -> dict:
        """Return magic stats based on cost."""
        return {"mana_power": self.cost * 2}
