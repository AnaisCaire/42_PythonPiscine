# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 10:17:49 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/16 10:35:42 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .basic import lead_to_gold
from ..potions import healing_potion

def philosophers_stone():
    return (
        f"Philosopher’s stone created using {lead_to_gold()}"
        f"and {healing_potion()}"
        )

def elixir_of_life():
    return "Elixir of life: eternal youth acheived!"