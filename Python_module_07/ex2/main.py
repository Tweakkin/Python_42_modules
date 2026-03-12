from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard

def main() -> None:
    print("=== DataDeck Ability System ===")
    print()

    # Create an elite card
    warrior = EliteCard("Arcane Warrior", 4, Rarity.LEGENDARY, 5, 10, 8)
    card_m = [m for m in dir(Card) if not m.startswith('_')]
    comb_m = [m for m in dir(Combatable) if not m.startswith('_')]
    magic_m = [m for m in dir(Magical) if not m.startswith('_')]
    print("EliteCard capabilities:")
    print(f"- Card: {card_m}")
    print(f"- Combatable: {comb_m}")
    print(f"- Magical: {magic_m}")

    print(f"\nPlaying {warrior.name} (Elite Card):\n")
    # play_result: dict = warrior.play({"mana": 10})
    # print(f"{play_result}")
    print("Combat phase:")
    attack_res: dict = warrior.attack("Enemy")
    print(f"Attack result: {attack_res}")
    defend_res: dict = warrior.defend(5)
    print(f"Defense result: {defend_res}")

    print("\nMagic phase:")
    spell_r: dict = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_r}")
    mana_ch: dict = warrior.channel_mana(3)
    print(f"Mana channel: {mana_ch}")

    print("Multiple interface implementation successful!")

if __name__ == "__main__":
    main()