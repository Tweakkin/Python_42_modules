import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self,
                        name_or_power: str | int | None = None) -> Card:
        try:
            if isinstance(name_or_power, str):
                creatures: dict[str, CreatureCard] = {
                    "dragon": CreatureCard("Fire Dragon", 5,
                                           Rarity.LEGENDARY, 7, 5),
                    "goblin": CreatureCard("Goblin Warrior", 2,
                                           Rarity.COMMON, 3, 2),
                }
                return creatures.get(
                    name_or_power.lower(),
                    CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
                )
            if isinstance(name_or_power, int):
                power: int = max(1, name_or_power)
                return CreatureCard("Fantasy Creature", power,
                                    Rarity.RARE, power + 2, power + 1)
            return CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
        except Exception:
            return CreatureCard("Default Creature", 1, Rarity.COMMON, 1, 1)

    def create_spell(self,
                     name_or_power: str | int | None = None) -> Card:
        try:
            if isinstance(name_or_power, str):
                spells: dict[str, SpellCard] = {
                    "fireball": SpellCard("Fireball", 4, Rarity.RARE,
                                          "damage"),
                    "heal": SpellCard("Healing Light", 3, Rarity.COMMON,
                                      "heal"),
                    "lightning": SpellCard("Lightning Bolt", 3, Rarity.RARE,
                                           "damage"),
                }
                return spells.get(
                    name_or_power.lower(),
                    SpellCard("Fireball", 4, Rarity.RARE, "damage")
                )

            if isinstance(name_or_power, int):
                power: int = max(1, name_or_power)
                return SpellCard("Arcane Blast", power, Rarity.RARE,
                                 "damage")

            return SpellCard("Fireball", 4, Rarity.RARE, "damage")
        except Exception:
            return SpellCard("Default Spell", 1, Rarity.COMMON, "damage")

    def create_artifact(self,
                        name_or_power: str | int | None = None) -> Card:
        try:
            if isinstance(name_or_power, str):
                artifacts: dict[str, ArtifactCard] = {
                    "mana_ring": ArtifactCard("Mana Ring", 2, Rarity.EPIC,
                                              5, "+2 mana per turn"),
                    "staff": ArtifactCard("Crystal Staff", 4,
                                          Rarity.LEGENDARY, 3,
                                          "+3 spell power"),
                    "crystal": ArtifactCard("Power Crystal", 3, Rarity.RARE,
                                            4, "+1 to all stats"),
                }
                return artifacts.get(
                    name_or_power.lower(),
                    ArtifactCard("Mana Ring", 2, Rarity.EPIC, 5,
                                 "+2 mana per turn")
                )

            if isinstance(name_or_power, int):
                power: int = max(1, name_or_power)
                return ArtifactCard("Magic Artifact", power, Rarity.RARE,
                                    power + 1, f"+{power} power")

            return ArtifactCard("Mana Ring", 2, Rarity.EPIC, 5,
                                "+2 mana per turn")
        except Exception:
            return ArtifactCard("Default Artifact", 1, Rarity.COMMON, 1,
                                "No effect")

    def create_themed_deck(self, size: int) -> dict:

        try:
            size = max(1, int(size))
            cards: list = []

            # Available creature types to randomly pick from
            creature_names: list = ["dragon", "goblin"]
            spell_names: list = ["fireball", "lightning", "heal"]
            artifact_names: list = ["mana_ring", "staff", "crystal"]

            for i in range(size):
                # Distribute cards: creatures, spells, artifacts
                # i % 3 cycles through 0, 1, 2, 0, 1, 2, ...
                #   0 → creature
                #   1 → spell
                #   2 → artifact
                remainder: int = i % 3

                if remainder == 0:
                    # random.choice() picks one random item from a list
                    name: str = random.choice(creature_names)
                    cards.append(self.create_creature(name))
                elif remainder == 1:
                    name = random.choice(spell_names)
                    cards.append(self.create_spell(name))
                else:
                    name = random.choice(artifact_names)
                    cards.append(self.create_artifact(name))

            return {
                "deck_size": len(cards),
                "cards": cards,
                "theme": "Fantasy"
            }
        except Exception as e:
            return {"error": f"Deck creation failed: {str(e)}"}

    def get_supported_types(self) -> dict:
        """
        List all card types this factory can create.
        """
        try:
            return {
                "creatures": ["dragon", "goblin"],
                "spells": ["fireball", "lightning", "heal"],
                "artifacts": ["mana_ring", "staff", "crystal"]
            }
        except Exception as e:
            return {"error": f"Failed to get types: {str(e)}"}
