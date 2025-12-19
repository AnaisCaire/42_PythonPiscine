# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 12:24:29 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/19 13:32:45 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    """Parent class for all garden plants"""
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    """A Plant that has a color and can bloom"""
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """Gives points to flowers"""
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

class GardenManager():
    """Manages, contains and oversees the whole collection of plants"""

    registory = []

    def __init__(self, owner):
        self.owner = owner
        self.plant = []
        self.stats = GardenManager.GardenStats()
        GardenManager.registory += 1

    def add_plant(self, plant):
        """Adds a plant to owners collection"""
        self.plant.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden.")
    
    def plant_grow(self, growth):
        """help all plants grow"""
        print(f"\n{self.owner} is helping all plants grow...")
        for p in self.plant:
            p.height += growth
        print(f"{p.name} grew {growth}cm")

    class GardenStats():
        """Just for reading information"""
        @staticmethod
        def get_type():
            """counts the plant types from the inheretence chain"""
            normal = flowering = prize = 0

            for manager in GardenManager.registory:
                for p in manager.plant:
                    if isinstance(p, Plant):
                        normal += 1
                    elif isinstance(p, FloweringPlant):
                        flowering += 1
                    else:
                        prize += 1
                print(f"\nPlant types: {normal} regular, {flowering} flowering and {prize} prize plants")
        
        @staticmethod
        def create_garden_network():
            """Give each owner a Garden Report"""
            for manager in GardenManager.registory:
                print(f"\n==== {manager.owner}'s Garden Report ====")
                print("Plants in Garden:")
                for p in manager.plant:
                    p.report()
                    GardenManager.GardenStats.get_type()

                    


if __name__ == "__main__":

    flowers = [("Marie", 14, "Red"), ("Dhali", 4, "purple"), ("Rose", 25, "Red")]
    flower_g = [FloweringPlant(*d) for d in flowers]
    
    plants = [("Oak", 500), ("Maple", 876)]
    plants_g = [Plant(*p) for p in plants]
    
    managers = ["jacob", "Ana", "Mathis", "Illy"]
    managers_append = [GardenManager(d) for d in managers]

    managers_append[0].add_plant(flower_g[0])
    managers_append[0].add_plant(plants_g[1])
    managers_append[1].add_plant(flower_g[1])
    managers_append[1].add_plant(flower_g[1])
    managers_append[2].add_plant(plants_g[0])
    managers_append[3].add_plant(flower_g[2])
    
    managers_append[0].plant_grow(2)
    GardenManager.GardenStats.create_garden_network()