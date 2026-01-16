# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    basic.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 10:17:38 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/16 10:20:02 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from alchemy.elements import create_fire, create_earth


def lead_to_gold():
    return f"Lead transumted to gold using {create_fire()}"


def stone_to_gem():
    return f"Stone transmuted to gem using {create_earth()}"