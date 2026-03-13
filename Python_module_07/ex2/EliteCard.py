from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Union


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: Union[str, Rarity],
                 attack: int, health: int, mana_pool: int) -> None:
        try:
            super().__init__(name, cost, rarity)
            # super calls Card bcs Card.__init__ is rge first
            # in the MRO
            self.attack_power: int = attack
            self.health: int = health
            self.mana_pool: int = mana_pool
            self.armor: int = 2
        except (ValueError, TypeError):
            super().__init__(name, cost, rarity)
            self.attack_power = 1
            self.health = 1
            self.mana_pool = 0
            self.armor = 2

    # Card interface implementation
    def play(self, game_state: dict) -> dict:
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
                "effect": "Elite card deployed with combat and magic abilities"
            }
        except Exception as e:
            return {"error": f"Failed to play {self.name}: {str(e)}"}

    def get_card_info(self) -> dict:
        """Override to include elite card stats."""
        try:
            info: dict = super().get_card_info()
            info["attack"] = self.attack_power
            info["health"] = self.health
            info["mana_pool"] = self.mana_pool
            return info
        except Exception as e:
            return {"error": f"Failed to get card info: {str(e)}"}

    # Combatable interface implementation

    def attack(self, target: object) -> dict:
        """ Implement Combatable's abstract attack method. """
        try:
            target_name: str = target.name if hasattr(target, "name") \
                else str(target)
            return {
                "attacker": self.name,
                "target": target_name,
                "damage": self.attack_power,
                "combat_type": "melee"
            }
        except Exception as e:
            return {"error": f"Attack failed: {str(e)}"}

    def defend(self, incoming_damage: int) -> dict:
        """ Implement Combatable's abstract defend method. """
        try:
            damage: int = max(0, int(incoming_damage))
            blocked: int = min(self.armor, damage)
            actual_damage: int = damage - blocked
            self.health -= actual_damage
            return {
                "defender": self.name,
                "damage_taken": actual_damage,
                "damage_blocked": blocked,
                "still_alive": self.health > 0
            }
        except Exception as e:
            return {"error": f"Defense failed: {str(e)}"}

    def get_combat_stats(self) -> dict:
        """Implement Combatable's abstract get_combat_stats method."""
        try:
            return {
                "attack": self.attack_power,
                "health": self.health,
                "armor": self.armor
            }
        except Exception as e:
            return {"error": f"Failed to get combat stats: {str(e)}"}

    # Magical interface implementation

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """ Implement Magical's abstract cast_spell method. """
        try:
            mana_cost: int = len(targets) * 2
            if self.mana_pool < mana_cost:
                return {
                    "caster": self.name,
                    "spell": spell_name,
                    "cast": False,
                    "reason": "Not enough mana"
                }
            self.mana_pool -= mana_cost
            target_names: list = []
            for t in targets:
                target_names.append(t if isinstance(t, str) else str(t))

            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": target_names,
                "mana_used": mana_cost
            }
        except Exception as e:
            return {"error": f"Spell cast failed: {str(e)}"}

    def channel_mana(self, amount: int) -> dict:
        """ Implement Magical's abstract channel_mana method. """
        try:
            channeled: int = max(0, int(amount))
            self.mana_pool += channeled
            return {
                "channeled": channeled,
                "total_mana": self.mana_pool
            }
        except Exception as e:
            return {"error": f"Mana channeling failed: {str(e)}"}

    def get_magic_stats(self) -> dict:
        """Implement Magical's abstract get_magic_stats method."""
        try:
            return {
                "mana_pool": self.mana_pool,
                # Elite cards use attack as spell power too
                "spell_power": self.attack_power
            }
        except Exception as e:
            return {"error": f"Failed to get magic stats: {str(e)}"}
