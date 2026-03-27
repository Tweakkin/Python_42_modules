import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'
        ),
        'ice_enchant': functools.partial(
            base_enchantment, power=50, element='ice'
        ),
        'lightning_enchant': functools.partial(
            base_enchantment, power=50, element='lightning'
        )
    }


@functools.lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast_spell(spell):
        return "Unknown spell"

    @cast_spell.register(int)
    def _(spell: int):
        return f"damage spell: {spell}"

    @cast_spell.register(str)
    def _(spell: str):
        return f"enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list):
        return f"multi-cast: {spell}"

    return cast_spell


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer([10, 20, 30, 40], 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
