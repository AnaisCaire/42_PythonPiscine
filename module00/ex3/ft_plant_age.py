# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 15:02:48 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 14:54:53 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    if (int(input("Enter plant age in days: ")) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
