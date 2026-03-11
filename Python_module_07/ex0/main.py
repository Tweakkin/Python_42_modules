from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard

def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    try:
        abstract_card = Card("Test", 1, "Common")
    except TypeError as e:
        pass

    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    play_result: dict = dragon.play({"mana": 6})
    print(f"Play result: {play_result}")
    print()

    goblin = CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 3, 2)
    print(f"Fire Dragon attacks {goblin.name}:")
    attack_result = dragon.attack_target(goblin)
    print(f"Attack result: {attack_result}")
    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")



if __name__ == "__main__":
    main()