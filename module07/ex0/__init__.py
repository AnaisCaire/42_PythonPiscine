# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acaire-d <acaire-d@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 09:32:34 by acaire-d          #+#    #+#              #
#    Updated: 2026/01/19 10:35:14 by acaire-d         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .Card import Card
from .CreatureCard import CreatureCard

__all__ = ["Card", "CreatureCard"]
