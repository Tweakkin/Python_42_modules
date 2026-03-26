from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Main demonstration function."""
    print("=== DataDeck Tournament Platform ===")
    print()

    # Create the platform
    platform = TournamentPlatform()

    # Create tournament cards
    dragon = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, Rarity.EPIC, 4, 6)

    # Register cards
    print("Registering Tournament Cards...\n")
    dragon_id: str = platform.register_card(dragon)
    wizard_id: str = platform.register_card(wizard)

    # Show card details
    print(f"{dragon.name} (ID: {dragon_id}):")
    # Prove multiple inheritance with isinstance
    interfaces: list = []
    if isinstance(dragon, Card):
        interfaces.append("Card")
    if isinstance(dragon, Combatable):
        interfaces.append("Combatable")
    if isinstance(dragon, Rankable):
        interfaces.append("Rankable")
    print(f"- Interfaces: {interfaces}")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")
    print()

    print(f"{wizard.name} (ID: {wizard_id}):")
    interfaces2: list = []
    if isinstance(wizard, Card):
        interfaces2.append("Card")
    if isinstance(wizard, Combatable):
        interfaces2.append("Combatable")
    if isinstance(wizard, Rankable):
        interfaces2.append("Rankable")
    print(f"- Interfaces: {interfaces2}")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")
    print()

    # Create a match
    print("Creating tournament match...")
    match_result: dict = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")
    print()

    # Show leaderboard
    print("Tournament Leaderboard:")
    leaderboard: list = platform.get_leaderboard()
    for entry in leaderboard:
        print(f"{entry['rank']}. {entry['name']} "
              f"- Rating: {entry['rating']} "
              f"({entry['record']})")
    print()

    # Show tournament report
    report: dict = platform.generate_tournament_report()
    print("Platform Report:")
    print(f"{report}")
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
