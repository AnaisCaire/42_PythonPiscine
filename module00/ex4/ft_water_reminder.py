# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 15:07:12 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 14:56:29 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    if (int(input("Days since last watering: ")) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
