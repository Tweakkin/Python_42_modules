from ex0.Card import Card, Rarity, CardType
from typing import Union

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Union[str, Rarity],
                 attack: int, health: int) -> None:
        try:
            super().__init__(name, cost, rarity)
            self.health: int = max(1, int(health))
            self.attack:  int = max(1, int(attack))
            self.type = CardType.CREATURE.value
        except (ValueError, TypeError):
            super().__init__(name, cost, rarity)
            self.attack = 1
            self.health = 1
            self.type = "Creature"
    def play(self, game_state: dict) -> dict:
        try:
            available_mana: int = game_state.get("mana", 0)

            if not self.is_playable(available_mana):
                return {
                    "card_played": self.name,
                    "mana_used": 0,
                    "effect": f"Not enoug mana to summon {self.name}"
                }
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        except Exception as e:
            return {"Error": f"Failed to play {self.name}: {str(e)}"}
    
    def get_card_info(self) -> dict:
        try:
            info: dict = super().get_card_info()
            info["attack"] = self.attack
            info["health"] = self.health
            return info
        except Exception as e:
            return {"Error": f"Failed to get card info {str(e)}"}
    
    def attack_target(self, target) -> dict:
        try:
            target_name: str = target.name if hasattr(target, "name") \
                else str(target)
            return {
                "attacker": self.name,
                "target": target_name,
                "damage_dealt": self.attack,
                "combat_resolved": True
            }
        except Exception as e:
            return {"Error": f"Attack failed: {str(e)}"}