from functools import wraps
import time
from typing import Any


def spell_timer(func: callable) -> callable:
    """
    • Create a decorator that measures function execution time
    • Print "Casting function_name..." before execution
    • Print "Spell completed in time seconds" after execution
    • Use functools.wraps to preserve original function metadata
    • Return the original function’s result
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__} ...")
        start_time: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """
    • Create a decorator factory that validates power levels
    • Check if the first argument (power) is >= min_power
    • If valid, execute the function normally
    • If invalid, return "Insufficient power for this spell"
    • Use functools.wraps properly
    """
    def decorator(func):
        @wraps(func)  # preserveds identity and metadata
        def wrapper(self, spell_name, power, *args, **kwargs):
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """
    • Create a decorator that retries failed spells
    • If function raises an exception, retry up to max_attempts times
    • Print "Spell failed, retrying... (attempt n/max_attempts)"
    • If all attempts fail, return
        "Spell casting failed after max_attempts attempts"
    • If successful, return the result normally
    """
    def decorator(func):
        @wraps(func)
        def wrapper(spell_name, power, *args, **kwargs):
            for i in range(max_attempts):
                try:
                    result = func(spell_name, power, *args, **kwargs)
                    if result != "Insufficient power for this spell":
                        return result
                except Exception:
                    pass  # to continue even if it fails
                power += 1
                print("Spell failed, retrying (+1 power)..."
                      f"(attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (name.isalpha() or name.isspace()) and len(name) >= 3:
            print(f"{name} is valid!")
            return True
        print(f"{name} is invalid")
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """ Cast spell and return the result """
        time.sleep(power/100)
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    # Master's Tower Test Data
    test_powers = [27, 22, 6, 7]
    spell_names = ['tsunami', 'shield', 'flash', 'freeze']
    mage_names = ['Kai', 'Riley', 'Morgan', 'Jordan', 'Nova', 'Zara']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("=== The Master’s Tower === \n")
    print("Testing spell timer...")

    @spell_timer
    @retry_spell(10)
    @power_validator(10)
    def casting_spell(spell_name: str, power: int) -> str:
        """ Cast spell and return the result """
        print(f"function name is: {spell_name}")
        time.sleep(power/100)
        return f"Result: {spell_name} cast!"

    cast_spell_test = casting_spell("FireBall", 18)
    print(cast_spell_test)
    print()
    power_level_test = casting_spell("SnowBall", 2)
    print(power_level_test)

    print("\nTesting validation name function...")
    instance = MageGuild()
    print("--- With valid names:")
    for mage in mage_names:
        instance.validate_mage_name(mage)
    print("--- With invalid names...")
    for names in invalid_names:
        instance.validate_mage_name(names)

    print("\nThe whole Mage class validation process...")
    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("bad spell", 5))
