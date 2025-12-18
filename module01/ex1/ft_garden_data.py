#!/usr/python/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 13:48:01 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/17 13:48:10 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.height_cm = height
        self.age_days = age

    def report(self):
        print(f"""plants name: {self.name}
the plants age is: {self.age_days} days
And its height: {self.height_cm} cm
--------------------------------""")


if __name__ == "__main__":
    david = Plant("Rose", 14, 5)
    maya = Plant("Tulip", 34, 18)
    ana = Plant("Monstera", 76, 3200)

    print("=== The Community Garden! ===\n")
    david.report()
    maya.report()
    ana.report()
    print("=== END ===\n")
