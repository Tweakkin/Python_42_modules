from abc import ABC, abstractmethod

class Card(ABC):
	def __init__(self, name: str, cost: int, rarity:str):
		try:
			self.name: int = str(name)
			self.cost: int = max(0, int(cost))
			self.rarity: str = str(rarity)
		except (ValueError, TypeError):
			self.name = "Unkown"
			self.cost = 0
			self.rarity "Common"

	@abstractmethod
	def play(self, game_state: dict):
		pass
	
	def get_card_info(self):
		try:
			return {
				"name": self.name,
				"cost": self.cost,
				"rarity": self.rarity,
			}
		except Exception as e:
			return {"Error": f"Failed to get card info: {str(e)}"}
	
	def is_playable(self, available_mana: int) -> bool:
		try:
			return int(available_mana) >= self.cost
		except Exception as e:
			return False