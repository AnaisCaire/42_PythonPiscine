# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    potions.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 15:29:27 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/15 18:13:23 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import alchemy.elements


def healing_potion():
    return (
        f"healing potion brewed with {alchemy.elements.create_fire()}"
        f"and {alchemy.elements.create_water()}"
        )


def strenght_potion():
    return (
        f"Strength potion brewed with {alchemy.elements.create_earth()}"
        f"and {alchemy.elements.create_fire()}"
        )


def invisibility_potion():
    return (
        f"Ïnvisibility potion brewed with {alchemy.elements.create_air}"
        f"and {alchemy.elements.create_water}"
        )


def wisdom_potion():
    return (
        f"Wisdom potion brewed with all elements: {alchemy.elements.create_water}"
        f"{alchemy.elements.create_earth}, {alchemy.elements.create_air}, "
        f"{alchemy.elements.create_fire}"
    )