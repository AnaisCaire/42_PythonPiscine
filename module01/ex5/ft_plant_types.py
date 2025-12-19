# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_s.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 09:55:18 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/18 12:12:38 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """Parent class"""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    """Plant with color and blooming"""
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def report(self):
        print(f"{self.name} (Flower) : {self.height} cm, {self.age} days, {self.color} color")
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")

class Tree(Plant):
    """Plant with trunk diameter and can produce shade"""
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def report(self):
            print(f"{self.name} (Tree) : {self.height} cm, {self.age} days, {self.trunk_diameter}cm diameter")
    def produce_shade(self):
        """shade is half of the diameter"""
        shade = self.trunk_diameter / 2
        print(f"{self.name} provides {shade} square meters of shade\n")

class Vegetable(Plant):
    """Plant with harvest season and nutritional value"""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def report(self):
            print(f"{self.name} (Vegetable) : {self.height} cm, {self.age} days, {self.harvest_season} harvest")
    def rich(self):
        print(f"the {self.name} is rich in: {self.nutritional_value}\n")

if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 18, 25, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 400, 1500, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 60, 120, "fall", "beta-carotene")

    plants = (rose, tulip, oak, maple, tomato, carrot)
    for plant in plants:
        plant.report()
        if isinstance(plant, Flower):
             plant.bloom()
        if isinstance(plant, Tree):
             plant.produce_shade()
        if isinstance(plant, Vegetable):
             plant.rich()