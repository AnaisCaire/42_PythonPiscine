# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 17:58:27 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 17:57:42 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:
    def __init__(self, name, age, height):
        self._name = name
        self._age = 0
        self._height = 0
        print(f"Plant created: {self._name}")
        self.set_height = height
        self.set_age = age

    @property
    def get_height(self):
        return self._height

    @get_height.setter
    def set_height(self, new_height):
        if (new_height <= 0):
            print(f"\nInvalid operation attempted: height {new_height} "
                  "[REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = new_height
        print(f"Height updated: {self._height}cm [OK]")

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, new_age):
        if (new_age <= 0):
            print(f"\nInvalid operation attempted: age {new_age} [REJECTED]\n")
            print("Security: Negative age rejected")
            return
        self._age = new_age
        print(f"Age updated: {self._age} days [OK]")

    def get_info(self):
        print(f"\nCurrent plant: {self._name} ({self._height}cm, {self._age} days)")


if __name__ == "__main__": 
    print("=== Garden Security System ===")
    demo = SecurePlant("Rose", 30, 25)
    demo.set_height = -5
    demo.get_info()
