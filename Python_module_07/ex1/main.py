from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.Card import Rarity

def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print()

    # Create different card types
    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, Rarity.RARE, "damage")
    crystal = ArtifactCard("Mana Crystal", 2, Rarity.COMMON, 3, "+1 mana per turn")

    # Build a DECK
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(dragon)
    deck.add_card(bolt)
    deck.add_card(crystal)

    # Show deck stats
    stats: dict = deck.get_deck_stats()
    print(f"Deck stats: {stats}")
    print()

    # Shuffle and Draw
    print("Drawing and playing cards:")
    deck.shuffle()

    game_state: dict = {"mana": 10}

    while True:
        card = deck.draw_card()
        if card is None:
            break
        print(f"Drew: {card.name} ({card.type})")
        result: dict = card.play(game_state)
        print(f"Play result: {result}")
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()