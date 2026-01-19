
class Plant:
    """
    blueprint for all plants with same attributes
    """
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.height_cm = height
        self.age_days = age

    def report(self):
        print(f"{self.name}: {self.height_cm}cm, {self.age_days} days old")


if __name__ == "__main__":
    david = Plant("Rose", 30, 25)
    maya = Plant("Sunflower", 45, 80)
    ana = Plant("Cactus", 120, 15)

    print("=== The Community Garden! ===")
    david.report()
    maya.report()
    ana.report()
