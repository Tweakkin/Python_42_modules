from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):
	"""
    A card that can be played, can fight, AND can be ranked.
	"""
    def __init__(self, name: str, cost: int, rarity: Union[str, Rarity],
                 attack: int, health: int) -> None:
        try:
            # Call Card's __init__ through super()
            # super() follows the MRO
            super().__init__(name, cost, rarity)

            # Combat attributes
            self.attack_power: int = max(1, int(attack))
            self.health: int = max(1, int(health))
            self.max_health: int = self.health  # Remember original health
            self.armor: int = 2

            # Tournament tracking attributes
            # These are NEW only TournamentCard has these
            self.wins: int = 0
            self.losses: int = 0
            self.rating: int = 1200  # Starting rating
        except (ValueError, TypeError):
            super().__init__(name, cost, rarity)
            self.attack_power = 1
            self.health = 1
            self.max_health = 1
            self.armor = 2
            self.wins = 0
            self.losses = 0
            self.rating = 1200
	
	# Card interface

    def play(self, game_state: dict) -> dict:
        """Implement Card's abstract play() method."""
        try:
            available_mana: int = game_state.get("mana", 0)
            if not self.is_playable(available_mana):
                return {
                    "card_played": self.name,
                    "mana_used": 0,
                    "effect": f"Not enough mana to play {self.name}"
                }
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Tournament card entered the arena"
            }
        except Exception as e:
            return {"error": f"Failed to play {self.name}: {str(e)}"}

    def get_card_info(self) -> dict:
        """Override Card's get_card_info to add tournament stats."""
        try:
            info: dict = super().get_card_info()
            info["attack"] = self.attack_power
            info["health"] = self.health
            info["rating"] = self.rating
            info["record"] = f"{self.wins}-{self.losses}"
            return info
        except Exception as e:
            return {"error": f"Failed to get card info: {str(e)}"}

	# Combatable interface

    def attack(self, target) -> dict:
        """
        Implement Combatable's abstract attack() method.

        Parameters:
            target: The thing being attacked

        Returns:
            dict: Attack results
        """
        try:
            target_name: str = target.name if hasattr(target, "name") \
                else str(target)
            return {
                "attacker": self.name,
                "target": target_name,
                "damage": self.attack_power,
                "combat_type": "tournament"
            }
        except Exception as e:
            return {"error": f"Attack failed: {str(e)}"}

    def defend(self, incoming_damage: int) -> dict:
        """
        Implement Combatable's abstract defend() method.

        Armor absorbs some damage. Remaining damage reduces health.

        Parameters:
            incoming_damage (int): How much damage is coming in

        Returns:
            dict: Defense results
        """
        try:
            damage: int = max(0, int(incoming_damage))
            blocked: int = min(self.armor, damage)
            actual_damage: int = damage - blocked
            self.health -= actual_damage
            return {
                "defender": self.name,
                "damage_taken": actual_damage,
                "damage_blocked": blocked,
                "remaining_health": self.health,
                "still_alive": self.health > 0
            }
        except Exception as e:
            return {"error": f"Defense failed: {str(e)}"}

    def get_combat_stats(self) -> dict:
        """Implement Combatable's abstract get_combat_stats() method."""
        try:
            return {
                "attack": self.attack_power,
                "health": self.health,
                "armor": self.armor
            }
        except Exception as e:
            return {"error": f"Failed to get combat stats: {str(e)}"}

	# Rankable Interface
    def calculate_rating(self) -> int:
        """
        Implement Rankable's abstract calculate_rating() method.

        Simple rating formula:
        - Start at base rating (1200)
        - Each win adds 16 points
        - Each loss subtracts 16 points

        This is a simplified version of the ELO rating system
        used in chess. Higher rating = better player/card.

        Returns:
            int: The calculated rating
        """
        try:
            self.rating = 1200 + (self.wins * 16) - (self.losses * 16)
            return self.rating
        except Exception as e:
            return self.rating

    def update_wins(self, wins: int) -> None:
        """
        Implement Rankable's abstract update_wins() method.

        Parameters:
            wins (int): Number of wins to add
        """
        try:
            self.wins += max(0, int(wins))
            self.calculate_rating()  # Recalculate after updating
        except (ValueError, TypeError):
            pass
		
    def update_losses(self, losses: int) -> None:
        """
        Implement Rankable's abstract update_losses() method.

        Parameters:
            losses (int): Number of losses to add
        """
        try:
            self.losses += max(0, int(losses))
            self.calculate_rating()  # Recalculate after updating
        except (ValueError, TypeError):
            pass

    def get_rank_info(self) -> dict:
        """Implement Rankable's abstract get_rank_info() method."""
        try:
            return {
                "name": self.name,
                "rating": self.rating,
                "wins": self.wins,
                "losses": self.losses,
                "record": f"{self.wins}-{self.losses}"
            }
        except Exception as e:
            return {"error": f"Failed to get rank info: {str(e)}"}

	# TournamentCard's own method not inherited
    def get_tournament_stats(self) -> dict:
        """
        Get complete tournament statistics.

        This combines info from ALL three interfaces into one report.
        Only TournamentCard has this method, it doesn't exist in
        Card, Combatable, or Rankable.

        Returns:
            dict: Complete tournament stats
        """
        try:
            return {
                "name": self.name,
                "card_info": self.get_card_info(),
                "combat_stats": self.get_combat_stats(),
                "rank_info": self.get_rank_info(),
                "interfaces": ["Card", "Combatable", "Rankable"]
            }
        except Exception as e:
            return {"error": f"Failed to get stats: {str(e)}"}

    def reset_health(self) -> None:
        """
        Reset health to max after a match.

        Without this, a card that took damage in match 1
        would start match 2 with reduced health — unfair!
        """
        self.health = self.max_health