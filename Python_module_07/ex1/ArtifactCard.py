from ex0.Card import Card, Rarity
from typing import Union

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Union[Rarity, str],
                 durability: int, effect: str) -> None:
        try:
            super().__init__(name, cost, rarity)
            self.durability: int = max(1, int(durability))
            self.effect: str = str(effect)
            self.is_active: bool = False
            self.type = "Artifact"
        except:
            super().__init__(name, cost)
            self.durability = 1
            self.effect = "No effect"
            self.is_active = False
            self.type = "Artifact"
    def play(self, game_state: dict) -> dict:
        try:
            available_mana: int = game_state.get("mana", 0)

            if not self.is_playable(available_mana):
                return{
                    "card_played": self.name,
                    "mana_used": 0,
                    "effect": f"Not enough mana to deploy {self.name}"
                }
            self.is_active = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Permanent: {self.effect}"
            }
        except Exception as e:
            return {"Error": f"Failed to deploy {self.name}: {str(e)}"}
    
    def get_card_info(self) -> dict:
        try:
            info: dict = super().get_card_info()
            info["durability"] = self.durability
            info["effect"] = self.effect
            info["is_active"] = self.is_active
            return info
        except Exception as e:
            return {"Error": f"Failed to get card info: {str(e)}"}
    
    def activate_ability(self) -> dict:
        try:
            if not self.is_active:
                return {
                    "artifact": self.name,
                    "activated": False,
                    "reason": "Artifact is not in play"
                }
            
            if self.durability <= 0:
                self.is_active = False
                return {
                    "artifact": self.name,
                    "activated": False,
                    "reason": "Artifact has been destroyed (no durability)"
                }
            self.durability -= 1
            result: dict = {
                "artifact" : self.name,
                "activated": True,
                "effect": self.effect,
                "remaining_durability": self.durability
            }

            if self.durability<= 0:
                self.is_active = False
                result["status"] = "Artifact destroyed after use"
            
            return result
        except Exception as e:
            return {"Error": f"Activation faield: {str(e)}"}