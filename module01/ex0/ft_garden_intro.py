#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 13:27:32 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/17 13:43:54 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_intro():
    """
    Display the info of my plant
    """
    plant: str = "Rose"
    height: int = 25
    age: int = 30
    print(
        f"=== Welcome to My Garden ===\n"
        f"Plant: {plant}\n"
        f"Height: {height}cm\n"
        f"Age: {age} days\n"
        "\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
