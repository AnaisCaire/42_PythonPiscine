# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 15:07:12 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/17 13:38:30 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = input("Days since last watering: ")
    if (int(days) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
