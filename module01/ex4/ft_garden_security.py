# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 17:58:27 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/19 13:29:29 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:
    def __init__(self, name, age, height):
        self._name = name
        self._age = 0
        self._height = 0
        self.get_name(name)
        self.set_age(age)
        self.set_height(height)

    def get_name(self, name):
        self._name = name
        print(f"\nCreated: {self._name}")

    def set_height(self, new_height):
        if (new_height <= 0):
            print(f"Invalid operation attempted: height {new_height} [REJECTED]")
            return
        self._height = new_height
        print(f"Height updated: {self._height}cm [OK]")

    def get_height(self):
        return self._height

    def set_age(self, new_age):
        if (new_age <= 0):
            print(f"\nInvalid operation attempted: age {new_age} [REJECTED]\n")
            return
        self._age = new_age
        print(f"Age updated: {self._age}days [OK]")

    def get_age(self):
        return self._age


if __name__ == "__main__":

    data = [("Rose", 3, 6), ("Oak", -200, 365), ("Cactus", 5, 90),
            ("Sunflower", 80, -45),
            ("Fern", 15, 10)]

    garden = [SecurePlant(*d) for d in data]
