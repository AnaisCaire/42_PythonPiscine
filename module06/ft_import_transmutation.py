
# Method 1: Full module import
# = better to see origin, +clarity
import alchemy.elements

# Method 2: Specific function import
# = use when dont need too much functions because the origin is less obvious
from alchemy.elements import create_water

# Method 3: Aliased import
from alchemy.potions import healing_potion as heal

# Method 4: Multiple imports in one line
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strenght_potion

if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===")
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print("\nMethod 2 - Specific function import:")
    print(f"create_water() {create_water()}")
    print("\nMethod 3 - Aliased import:")
    print(f"heal {heal()}")
    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strenght_potion()}")

    print("\nAll import transmutation methods mastered!")
