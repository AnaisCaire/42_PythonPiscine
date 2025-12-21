# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 17:28:45 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 15:21:05 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        unit = "packets available"
    if unit == "grams":
        unit = "grams total"
    if unit == "area":
        unit = "square meters"
    else:
        "Unknown unit type"
    print(seed_type.capitalize(), "seeds:", quantity, unit)
