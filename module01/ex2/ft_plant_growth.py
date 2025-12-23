# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 14:28:34 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 16:47:39 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.height_cm = height
        self.age_days = age

    def age(self, days: int):
        self.age_days += days

    def grow(self, days: int):
        self.height_cm += 1 * days

    def get_info(self):
        print(f"{self.name}: {self.height_cm:.2f} cm, {self.age_days} days")


if __name__ == "__main__":
    david = Plant("Rose", 30, 25)
    maya = Plant("Tulip", 34, 18)
    ana = Plant("Monstera", 76, 3200)
    davidinit = david.height_cm
    mayainit = maya.height_cm
    anainit = ana.height_cm
    print("=== Day 1 ===")
    david.age(0)
    david.grow(0)
    david.get_info()
    print("=== Day 7 ===")
    david.age(6)
    david.grow(6)
    david.get_info()
    """ for day in range(1, 8):
        print(f"=== Day {day} ===")
        david.grow(1)
        david.age(1)
        david.get_info()
        maya.grow(0.1)
        maya.age(1)
        maya.get_info()
        ana.grow(2)
        ana.age(1)
        ana.get_info()
        print("\n") """
print(f"Growth this week: +{david.height_cm - davidinit}")
# print(f"the total height gained of maya's is: {maya.height_cm - mayainit:.2f}")
# print(f"the total height gained of david's is: {ana.height_cm - anainit}")
