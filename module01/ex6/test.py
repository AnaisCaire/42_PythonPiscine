# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 13:02:47 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/19 13:21:26 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:
    """Base class for all garden inhabitants"""
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    """Plant specialized with flowering capabilities"""
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    """The highest tier in the plant family tree"""
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points


class GardenManager:
    """Manages collections of plants and coordinates analytics"""

    # Class-level variable to track across all instances
    total_gardens = 0

    class GardenStats:
        """Nested helper for calculating garden statistics"""
        @staticmethod
        def get_type_summary(plants: list) -> str:
            """Analyzes the inheritance chain to count types"""
            reg, flow, prize = 0, 0, 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flow += 1
                else:
                    reg += 1
            return f"{reg} regular, {flow} flowering, {prize} prize flowers"

    def __init__(self, owner_name: str):
        self.owner = owner_name
        self.plants = []
        self.stats_helper = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant):
        """Instance method to add a plant"""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden.")

    def help_all_grow(self, amount: int = 1):
        """Simulates growth for all plants in the collection"""
        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.height += amount
            print(f"{p.name} grew {amount}cm")

    @classmethod
    def create_garden_network(cls):
        """Class method working on the manager type itself["""
        print("Garden network initialized.")
        return cls.total_gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility function to validate height data"""
        return height > 0

    def report(self):
        """Displays the organized analytics report"""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            info = f"{p.name}: {p.height}cm"
            if isinstance(p, FloweringPlant):
                status = "(blooming)" if p.is_blooming else "(budding)"
                info += f", {p.color} flowers {status}"
            if isinstance(p, PrizeFlower):
                info += f", Prize points: {p.points}"
            print(info)

        summary = self.stats_helper.get_type_summary(self.plants)
        print(f"Plants added: {len(self.plants)}")
        print(f"Plant types: {summary}")


if __name__ == "__main__":
    # Demo as requested in Example
    print("Garden Management System Demo")

    alice_garden = GardenManager("Alice")

    # Adding different types from the family tree
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    print()
    alice_garden.help_all_grow(1)
    print()

    alice_garden.report()

    # Utility and Class level tests
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
