"""
This exercise is about learning higher-order functions
functions that take other functions as arguments and return new functions
"""


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    takes two functions and returns one that calls both
    and returns their results as a tuple
    """
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both arguments must be callable (functions)")
    return lambda *args: (spell1(*args), spell2(*args))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    wraps a function and multiplies its output by a given multiplier
    """
    if not callable(base_spell):
        raise TypeError("argument must be callable (functions)")
    return lambda *args: base_spell(*args) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    wraps a function so it only runs if a condition function returns True
    """
    if not callable(condition) or not callable(spell):
        raise TypeError("Both arguments must be callable (functions)")
    return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"


def spell_sequence(spells: list) -> callable:
    """
    takes a list of functions and returns one
    that calls all of them and collects results in a list
    """
    if not all(callable(spell) for spell in spells):
        raise TypeError("All items in spells must be callable (functions)")
    return lambda *args: [spell(*args) for spell in spells]


if __name__ == "__main__":
    def fireball(target): return f"Fireball hits {target}"
    def heal(target): return f"Heals {target}"
    try:
        print("\nTesting spell combiner...")
        combined = spell_combiner(fireball, heal)
        result = combined("Dragon")
        print(result)
        print(f"Combined spell result: {result[0]}, {result[1]}")

        print("\nTesting power amplifier...")
        def base_spell(x): return 10
        mega = power_amplifier(base_spell, 3)
        print(f"Original: {base_spell('x')}, Amplified: {mega('x')}")
    except TypeError as e:
        print(f"Error: {e}")
