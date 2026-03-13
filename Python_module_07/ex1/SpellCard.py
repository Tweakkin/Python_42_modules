from ex0.Card import Card, Rarity, CardType
from typing import Union


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Union[str, Rarity],
                 effect_type: str) -> None:

        try:
            super().__init__(name, cost, rarity)
            valid_types: list = ["damage", "heal", "buff", "debuff"]
            self.effect_type: str = effect_type if effect_type in valid_types \
                else "damage"
            self.type = CardType.SPELL.value
        except Exception:
            super().__init__(name, cost, rarity)
            self.effect_type = "damage"
            self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        try:
            available_mana: int = game_state.get("mana", 0)
            if not self.is_playable(available_mana):
                return {
                    "card_played": self.name,
                    "mana_used": 0,
                    "effect": f"Not enough mana to cast {self.name}"
                }
            effect_msgs: dict = {
                "damage": f"Deal {self.cost} damage to target",
                "heal": f"Restore {self.cost} health to target",
                "buff": f"Increase target stats by {self.cost}",
                "debuff": f"Decrease enemy stats by {self.cost}"
            }
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": effect_msgs.get(self.effect_type,
                                          "Unkown spell effect")
            }
        except Exception as e:
            return {"Error": f"Failed to cast {self.name}: {str(e)}"}

    def get_card_info(self) -> dict:
        try:
            info: dict = super().get_card_info()
            info["effect_type"] = self.effect_type
            return info
        except Exception as e:
            return {"Error": f"Failed to get card info: {str(e)}"}

    def resolve_effect(self, targets: list) -> dict:

        try:
            target_names: list = []
            for t in targets:
                target_names.append(t.name if hasattr(t, "name") else str(t))

            return {
                "spell": self.name,
                "effect_type": self.effect_type,
                "targets_affectes": target_names,
                "total_targets": len(target_names),
                "resolved": True
            }
        except Exception as e:
            return {"Error": f"Spell resolution failes: {str(e)}"}
