"""
Demonstrates decorator creation, parameterized decorators
retry logic, and @staticmethod usage.
"""

import functools
import time


def spell_timer(func: callable) -> callable:
    """
    a function that takes another function as input
    wraps it with timing logic, and returns the wrapped version
    """

    # Copies func's __name__, __doc__, etc. onto the wrapper
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start, 3)
        print(f"Spell completed in {elapsed} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """
    a decorator factory (a.k.a. parameterized decorator)
    it's a function that takes a config argument (min_power)
    and returns a decorator.
    """

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0] if args else kwargs.get('power', 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """
    Decorator factory that retries a function up to max_attempts
    times if it raises an exception.
    """

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return (
                f"Spell casting failed after {max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    """Guild class demonstrating @staticmethod and decorated methods."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Checks if a mage name is valid:
        at least 3 characters, only letters and spaces.
        """
        return (
            len(name) >= 3
            and all(c.isalpha() or c == ' ' for c in name)
        )

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with the given name and power level."""
        @power_validator(min_power=10)
        def _cast(power_level: int) -> str:
            return (
                f"Successfully cast {spell_name} "
                f"with {power_level} power"
            )
        return _cast(power)


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Thunder", 5))
