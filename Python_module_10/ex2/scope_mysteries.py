"""
This exercise is about learning closures and variable scope
specifically how inner functions can remember and modify variables
from their enclosing function.
"""


def mage_counter() -> callable:
    """
    returns a counter function that remembers and increments
    a count variable using nonlocal
    """

    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """
    returns a function that keeps a running total
    modifying it with nonlocal each time it's called.
    """

    total = initial_power

    def accumulate(amount):
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    """
    returns a function that remembers the enchantment_type string
    (read-only closure, no nonlocal needed).
    """
    def enchant(item_name):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict:
    """
     returns a dict of store/recall
    functions that share access to a private memory
    dict (mutable object, so no nonlocal needed either).
    """

    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
