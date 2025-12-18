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
    plant: str = "Rose"
    height: int = 32
    age: int = 2
    print(f"the plant type is: {plant}")
    print(f"the plant's height is: {height} cm")
    print(f"the plant's age is: {age} days")


if __name__ == "__main__":
     print("=== Here is my Graden ! ===\n")
     ft_garden_intro()
     print("\n=== end of program ===")
