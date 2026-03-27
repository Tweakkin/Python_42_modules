def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulate(amount):
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict:
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
