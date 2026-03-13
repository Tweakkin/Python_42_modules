from typing import Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Game orchestrator — connects factory and strategy.

    This is NOT abstract. It's a regular class.
    It doesn't create cards itself — it asks the factory.
    It doesn't decide how to play — it asks the strategy.
    It just CONNECTS the two and keeps track of what happened.
    """

    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.hand: list = []          # Cards in the player's hand
        self.battlefield: list = []   # Cards on the field
        self.turns_played: int = 0    # How many turns have been simulated
        self.total_damage: int = 0    # Total damage dealt across all turns
        self.cards_created: int = 0   # Total cards created by factory

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Plug in a factory and strategy.
        """
        try:
            self.factory = factory
            self.strategy = strategy
        except Exception as e:
            print(f"  Engine configuration error: {str(e)}")

    def simulate_turn(self) -> dict:
        """
        Simulate one turn of the game.

        Steps:
        1. Use the FACTORY to create some cards for the hand
        2. Use the STRATEGY to decide how to play them
        3. Record what happened
        4. Return a summary

        The engine doesn't know WHAT cards are created (factory decides)
        or HOW they're played (strategy decides). It just connects them.

        Returns:
            dict: Summary of what happened this turn
        """
        try:
            # Check that engine is configured
            if self.factory is None or self.strategy is None:
                return {"error": "Engine not configured. "
                        "Call configure_engine() first."}

            # Step 1: Factory creates cards for the hand
            # The engine says "give me a creature, a spell, an artifact"
            # It has NO idea what specific cards it will get
            self.hand = [
                self.factory.create_creature("dragon"),
                self.factory.create_creature("goblin"),
                self.factory.create_spell("lightning"),
            ]
            self.cards_created += len(self.hand)

            # Step 2: Strategy decides how to play them
            # The engine says "here's the hand, here's the field, GO"
            # It has NO idea what the strategy will do
            turn_result: dict = self.strategy.execute_turn(
                self.hand, self.battlefield
            )

            # Step 3: Record what happened
            self.turns_played += 1
            damage_this_turn: int = turn_result.get("damage_dealt", 0)
            self.total_damage += damage_this_turn

            return turn_result
        except Exception as e:
            return {"error": f"Turn simulation failed: {str(e)}"}

    def get_engine_status(self) -> dict:
        """
        Get a report of everything the engine has done.

        Returns:
            dict: Overall game statistics
        """
        try:
            strategy_name: str = "None"
            if self.strategy is not None:
                strategy_name = self.strategy.get_strategy_name()

            return {
                "turns_simulated": self.turns_played,
                "strategy_used": strategy_name,
                "total_damage": self.total_damage,
                "cards_created": self.cards_created
            }
        except Exception as e:
            return {"error": f"Status check failed: {str(e)}"}
