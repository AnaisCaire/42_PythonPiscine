# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Card.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acaire-d <acaire-d@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 09:32:39 by acaire-d          #+#    #+#              #
#    Updated: 2026/01/19 10:12:15 by acaire-d         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod


class Card(ABC):
    """The abstract foundation class"""
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity  = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Give the play results"""
        pass

    def get_card_info(self):
        pass

    def is_playable(self, available_mana: int) -> bool:
        """Checks if there is more than 5 mana to be playable"""
        if available_mana > 6:
            print("Playable : True")
            return True
        else:
            print(f"Testing insufficient mana ({available_mana} available):")
            print("Playable : False")
            return False
