# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 17:23:08 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/11 17:44:34 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    name = input("Enter garden name: ")
    nb = int(input("Enter number of plants: "))
    print(f"Garden: {name}")
    print(f"Plants: {nb}")
    print("Status: Good Garden GG!")