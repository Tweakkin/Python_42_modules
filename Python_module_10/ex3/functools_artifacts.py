"""
This exercise is about learning the functools module
Python's standard library for working with HOFs
"""

import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    uses functools.reduce() to combine a list of values
    into a single result by repeatedly applying an operation
    (add, multiply, max, min). Also uses the operator module
    """

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    uses functools.partial() to create pre-configured versions of a
    function with some arguments already filled in
    (like "fire with power 50").
    """

    if not callable(base_enchantment):
        raise TypeError("Argument must be callable!")
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
    """
    uses @functools.lru_cache() as a decorator to automatically
    cache/memoize results
    so recursive Fibonacci doesn't recompute the same values.
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """
    uses @functools.singledispatch to create a function
    that behaves differently
    depending on the type of its argument (int, str, list).
    """

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
    try:
        print("\nTesting spell reducer...")
        print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
        print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
        print(f"Max: {spell_reducer([10, 20, 30, 40], 'max')}")

        print("\nTesting memoized fibonacci...")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except TypeError as e:
        print(f"Error: {e}")
