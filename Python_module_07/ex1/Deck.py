import random
from typing import Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        try:
            if isinstance(card, Card):
                self.cards.append(card)
            else:
                print(f"Warning: {card} is not a valid Card")
        except Exception as e:
            print(f"Error adding card: {str(e)}")

    def remove_card(self, card_name: str) -> bool:
        try:
            for i, card in enumerate(self.cards):
                if card.name == card_name:
                    self.cards.pop(i)
                    return True
            return False
        except Exception as e:
            print(f"Error: removing card {str(e)}")
            return False

    def shuffle(self) -> None:
        try:
            random.shuffle(self.cards)
        except Exception as e:
            print(f"Error shuffling deck: {str(e)}")

    def draw_card(self) -> Optional[Card]:
        try:
            if len(self.cards) == 0:
                return None
            return self.cards.pop()
        except Exception as e:
            print(f"Error drawing card: {str(e)}")
            return None

    def get_deck_stats(self) -> dict:
        try:
            total: int = len(self.cards)
            creatures: int = sum(1 for c in self.cards
                                 if isinstance(c, CreatureCard))
            spells: int = sum(1 for c in self.cards
                              if isinstance(c, ArtifactCard))
            artifacts: int = sum(1 for c in self.cards
                                 if isinstance(c, ArtifactCard))
            avg_cost: float = 0.0
            if total > 0:
                avg_cost = sum(c.cost for c in self.cards) / total
                avg_cost = round(avg_cost, 1)

            return {
                "total_cards": total,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": avg_cost
            }
        except Exception as e:
            return {"error": f"Failed to get deck stats: {str(e)}"}
