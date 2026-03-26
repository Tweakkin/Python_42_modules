from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """Main demonstration function."""
    print("=== DataDeck Game Engine ===")
    print()

    # Create the factory and strategy
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    # Configure the Engine
    print("Configuring Fantasy Card Game...")
    print(f"Factory: {FantasyCardFactory.__name__}")
    print(f"Strategy: {AggressiveStrategy.__name__}")
    # Show what the factory can create
    print(f"Available types: {factory.get_supported_types()}")
    print()

    # Create and configure the Engine
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    # Stimulate a trun
    hand: list = [
        factory.create_creature("dragon"),
        factory.create_creature("goblin"),
        factory.create_spell("lightning")
    ]
    print("Simulating aggressive turn...")
    print("Hand: ")
    for h in hand:
        print(f"-{h.name} ({h.cost})")

    # Run the actual turn
    print("\nTurn execution:")
    turn_result: dict = engine.simulate_turn()
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result}")
    print()

    # Game report
    report: dict = engine.get_engine_status()
    print("Game Report:")
    print(report)

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
