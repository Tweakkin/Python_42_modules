from ex0.Card import Card

class CreatureCard(Card):
	def __init__(self, name: str, cost: int, rarity: str,
				 attack: int, health, int) -> None:
		try:
			super().__init__(name, cost, rarity)
			self.health: int = max(1, int(health))
			self.attack:  int = max(1, int(attack))
		except (ValueError, TypeError):
			super().__init__(name, cost, rarity)
			self.attack = 1
			self.health = 1
	def play(self, game_state: dict) -> dict:
		try:
			available_mana: int = game_state.get("mana", 0)

			if not self,is_playable(available_mana):
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