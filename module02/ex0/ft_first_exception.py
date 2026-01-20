
def check_temperature(temp_str: str):
    """
    Makes sure the temperature is valid for plants
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")


def test_temperature_input():
    """
    Small tester of 4 cases
    """
    temp = ["25", "abc", "100", "-50"]
    for t in temp:
        print("\nTesting temperature:", t)
        check_temperature(t)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
    print("\nAll tests completed - program didn't crash!")
