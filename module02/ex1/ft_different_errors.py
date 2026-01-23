
def garden_operations(error_type: str):
    """
    Performs specific actions that triggers common Python errors.
    """
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        10 / 0
    elif error_type == "file":
        open("missing.txt", "r")
    elif error_type == "key":
        plant_dict = {"Rose": 1}
        return plant_dict["Sunflower"]


def test_error_types():
    """
    Tests and handles various garden operation errors.
    """
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("zero")
    except (KeyError, FileNotFoundError, ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()
