# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    validator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 10:50:32 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/16 11:00:48 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def validate_ingredients(ingredients: str) -> str:
    
    valid = ["fire", "water", "earth", "air"]
    for element in valid:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
