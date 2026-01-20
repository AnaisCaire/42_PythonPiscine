
class GardenError(Exception):
    """
    A basic error for garden problems.
    """
    def __init__(self, message="Caught a garden error"):
        self.message = message
        super().__init__(message)
    pass


class PlantError(GardenError):
    """
    For problems with plants (inherits from GardenError).
    """
    def __init__(self, message="Plant error"):
        super().__init__(message)
    pass


class WaterError(GardenError):
    """
    For problems with watering (inherits from GardenError).
    """
    def __init__(self, message="A watering-related error occurred"):
        super().__init__(message)
    pass


def test_custom_errors():
    """
    Demonstrates raising and catching custom garden errors.
    """
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError("the tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    errors = [PlantError("the tomato plant is wilting!"),
              WaterError("Not enough water in the tank!")]

    for err in errors:
        try:
            raise err
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
