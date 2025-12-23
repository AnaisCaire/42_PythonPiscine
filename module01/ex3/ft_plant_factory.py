# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 15:15:15 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 16:57:52 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created {self.name}: ({self.height}cm, {self.age} days)")


def ft_plant_factory():
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)]

    garden = [Plant(*d) for d in data]

    print("=== Plant Factory Output ===")
    for plant in garden:
        plant.get_info()
    print(f"\nTotal plants created: {len(garden)}")


if __name__ == "__main__":
    ft_plant_factory()
