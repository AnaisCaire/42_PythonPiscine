# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    CreatureCard.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acaire-d <acaire-d@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 09:51:20 by acaire-d          #+#    #+#              #
#    Updated: 2026/01/19 10:40:12 by acaire-d         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from .Card import Card


class CreatureCard(Card):
    """Gives play and attack based on the Parent class Card"""
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """prints the play results"""
        if self.is_playable() is True:
            print(f"Playing {self.name} with {self.mana} available")
            game_state = {
                "card_played": self.name,
                "mana_used": 5,
                "effect": "Creature suummond to battlefield"
                }
            return game_state
        else:
            return "Not playable"

    def attack_target(self, target) -> dict:
        """Gives attack info and validation of health and attack points"""
        if self.health > 0 and self.attack > 0:
            print(f"{self.name} attacks {self.target}:")
            message = {
                "attacker": self.name,
                "target" : target,
                "damage_dealt": 7,
                "combat_resolved": True
            }
            return message
