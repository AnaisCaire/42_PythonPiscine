# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 15:15:15 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/17 18:37:16 by anaiscaire       ###   ########.fr        #
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
    # define data
    data = [("Rose", 3, 6), ("Oak", 200, 365), ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 10)]

    # add to class plant format
    garden = [Plant(*d) for d in data]
    
    print("Plant facotry output :\n")
    for plant in garden:
        plant.get_info()
    print(f"\nThere is {len(garden)} plants created !")


if __name__ == "__main__":
    ft_plant_factory()
