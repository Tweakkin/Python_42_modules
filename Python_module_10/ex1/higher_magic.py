def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args: (spell1(*args), spell2(*args))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args: base_spell(*args) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"


def spell_sequence(spells: list) -> callable:
    return lambda *args: [spell(*args) for spell in spells]


if __name__ == "__main__":
    def fireball(target): return f"Fireball hits {target}"
    def heal(target): return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(result)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("Testing power amplifier...")
    def base_spell(x): return 10
    mega = power_amplifier(base_spell, 3)
    print(f"Original: {base_spell('x')}, Amplified: {mega('x')}")
