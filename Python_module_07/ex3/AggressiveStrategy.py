from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    """ Concrete strategy that prioritizes attacking and damage. """

    def execute_turn(self, hand: list, battlefield: list) -> dict:

        try:
            cards_played: list = []
            mana_used: int = 0
            total_mana: int = 10
            damage_dealt: int = 0

            def get_cost(card):
                if hasattr(card, 'cost'):
                    return card.cost
                else:
                    return 5
            
            sorted_hand: list = sorted(hand, key=get_cost)
            for card in sorted_hand:
                card_cost: int = getattr(card, 'cost', 5)
                card_name: str = getattr(card, 'name', str(card))
                card_attack: int = getattr(card, 'attack', card_cost)

                if mana_used + card_cost <= total_mana:
                    cards_played.append(card_name)
                    mana_used += card_cost
                    damage_dealt += card_attack

            return {
                "strategy": self.get_strategy_name(),
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": ["Enemy Player"],
                "damage_dealt": damage_dealt
            }
        except Exception as e:
            return {"error": f"Turn execution failed: {str(e)}"}

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        try:
            return list(available_targets)
        except Exception as e:
            return []