from functools import wraps
import time
from typing import Callable, Any


def spell_timer(func: callable) -> callable:
    """
    • Create a decorator that measures function execution time
    • Print "Casting function_name..." before execution
    • Print "Spell completed in time seconds" after execution
    • Use functools.wraps to preserve original function metadata
    • Return the original function’s result
    """
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
        @wraps(func) # preserveds identity and metadata
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
    • If all attempts fail, return "Spell casting failed after max_attempts attempts"
    • If successful, return the result normally
    """
    pass


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    @spell_timer
    @power_validator(20)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """ Cast spell and return the result """
        print(f"function name is: {spell_name}")
        time.sleep(power/10)
        return f"Result: {spell_name} cast!"


if __name__ == "__main__":
    print("=== The Master’s Tower === \n")
    print("Testing spell timer...")

    instance = MageGuild()
    cast_spell_test = instance.cast_spell("FireBall", 28)
    print(cast_spell_test)
    print()
    power_level_test = instance.cast_spell("SnowBall", 8)
    print(power_level_test)
