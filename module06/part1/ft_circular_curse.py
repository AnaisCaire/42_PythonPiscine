# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_circular_curse.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 11:11:25 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/16 11:29:50 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import alchemy.grimoire as grimoire

print("\n=== Circular Curse Breaking ===")

print("\nTesting ingredient validation:")

print(
    f'validate_ingredients("fire air"): '
    f'{grimoire.validate_ingredients("fire air")}'
)
print(
    f'validate_ingredients("dragon scales"): '
    f'{grimoire.validate_ingredients("dragon scales")}'
)

print("\nTesting spell recording with validation:")
print(
    f'record_spell("Fireball", "fire air"): '
    f'{grimoire.record_spell("Fireball", "fire air")}'
)
print(
    f'record_spell("Dark Magic", "shadow"): '
    f'{grimoire.record_spell("Dark Magic", "shadow")}'
)

print("\nTesting late import technique:")
print(
    f'record_spell("Lightning", "air"): '
    f'{grimoire.record_spell("Lightning", "air")}'
)

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
