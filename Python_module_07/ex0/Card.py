from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Union[str, Rarity]):
        try:
            self.name: int = str(name)
            self.cost: int = max(0, int(cost))
            if isinstance(rarity, Rarity):
                self.rarity: Rarity = rarity
            else:
                self.rarity = Rarity(rarity)
        except (ValueError, TypeError):
            self.name = "Unkown"
            self.cost = 0
            self.rarity = Rarity.COMMON

    @abstractmethod
    def play(self, game_state: dict):
        pass
    
    def get_card_info(self):
        try:
            return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity.value,
                "type": self.type
            }
        except Exception as e:
            return {"Error": f"Failed to get card info: {str(e)}"}
    
    def is_playable(self, available_mana: int) -> bool:
        try:
            return int(available_mana) >= self.cost
        except Exception as e:
            return False