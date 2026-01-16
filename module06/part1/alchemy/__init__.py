# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 09:31:42 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/15 09:49:50 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

__version__ = "1.0.0"
__author__ = "Master Pythonicus"


from .elements import create_fire, create_water
__all__ = ["create_fire", "create_water"]
