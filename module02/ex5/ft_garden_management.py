
class GardenError(Exception):
    """A basic error for garden problems."""
    def __init__(self, message="Caught a garden error"):
        self.message = message
        super().__init__(message)
    pass


class PlantError(GardenError):
    """For problems with plants (inherits from GardenError)."""
    def __init__(self, message="Plant error"):
        super().__init__(message)
    pass


class WaterError(GardenError):
    """For problems with watering (inherits from GardenError)."""
    def __init__(self, message="watering-related error"):
        super().__init__(message)
    pass


class SunlightError(GardenError):
    """For problems with sunlight"""
    pass


class GardenManager:
    """
    the Garden Manager system with error handling
    """
    def __init__(self):
        self.garden = []

    def add_plant(self, plant_name, water_level, sunlight):
        """
        Adds the plant, the water level and sunlight hours in the garden
        """
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
        except PlantError as e:
            print(f"Error adding plant: {e}")
        else:
            individual_plant = {"name": plant_name,
                                "water": water_level,
                                "sun": sunlight}
            self.garden.append(individual_plant)
            print(f"Added {plant_name} successfully")
        return self

    def water_plants(self):
        """
        Waters every plant in the garden
        """
        try:
            for p in self.garden:
                try:
                    if not p['name']:
                        raise WaterError("Cannot water None - invalid plant!")
                    print(f"Watering {p['name']} - success")
                except WaterError as e:
                    print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")
        return self

    def check_plant_health(self, plant_name):
        """
        Finds the plant in the garden and checks its stats.
        """
        target_plant = None
        for plant in self.garden:
            if plant["name"] == plant_name:
                target_plant = plant
                break
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            if target_plant is None:
                raise PlantError(f"Plant '{plant_name}' not found")
        except PlantError as e:
            print(f"Error: {e}")
            return

        water_level = target_plant["water"]
        sunlight = target_plant["sun"]

        try:
            if water_level > 10:
                raise WaterError(
                    f"Water level {water_level} is too high (max 10)")
            elif water_level < 1:
                raise WaterError(
                    f"Water level {water_level} is too low (max 1)")
        except WaterError as e:
            print(f"Error checking {plant_name}: {e}")
            return
        try:
            if sunlight > 12:
                raise SunlightError(
                    f"Sunlight hours {sunlight} is too high (max 12)")
            if sunlight < 2:
                raise SunlightError(
                    f"Sunlight hours {sunlight} is too low (min 2)")
        except SunlightError as e:
            print(f"Error checking {plant_name}: {e}")
            return
        print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight})")
        return self


def tester():
    print("=== Garden Management System ==")
    print("\nAdding plants to garden...")
    demo = GardenManager()
    demo = demo.add_plant("tomato", 5, 8)
    demo = demo.add_plant("lettuce", 15, 6)
    demo = demo.add_plant("", 8, 3)
    print("\nWatering plants...")
    demo = demo.water_plants()

    print("\nChecking plant health...")
    demo.check_plant_health("tomato")
    demo.check_plant_health("lettuce")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enought water in the tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    tester()
