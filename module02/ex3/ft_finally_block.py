
def water_plants(plant_list):
    try:
        print("Opening watering system")
        for p in plant_list:
            if p is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {p}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(plant_list=["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(plant_list=["tomato", None])

    print("\nCleanup always happens, even with erorrs!")


if __name__ == "__main__":
    test_watering_system()
