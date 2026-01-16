# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spellbook.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 10:50:21 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/16 11:07:49 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    res = validate_ingredients(ingredients)
    if "VALID" in res:
        return f"Spell recorded: {spell_name} ({res})"
    else:
        return f"Spell rejected: {spell_name} ({res})"

    
    