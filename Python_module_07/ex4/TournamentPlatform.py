from ex4.TournamentCard import TournamentCard

class TournamentPlatform:

	def __init__(self) -> None:
        """Initialize an empty tournament platform."""
        self.cards: dict = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a card in the tournament.

        Each card gets a unique ID based on its name.
        The ID is used to look up cards for matches.

        Parameters:
            card (TournamentCard): The card to register

        Returns:
            str: The unique ID assigned to this card

        How the ID is generated:
            "Fire Dragon" → "fire_dragon_001"
            1. Take the name: "Fire Dragon"
            2. Lowercase it: "fire dragon"
            3. Replace spaces with underscores: "fire_dragon"
            4. Add a number suffix: "fire_dragon_001"
        """
        try:
            if not isinstance(card, TournamentCard):
                return "Error: Only TournamentCards can be registered"

            base_id: str = card.name.lower().replace(" ", "_")

            card_number: int = len(self.cards) + 1
            card_id: str = f"{base_id}_{card_number:03d}"
            # Store the card
            self.cards[card_id] = card

            return card_id
        except Exception as e:
            return f"Error: Registration failed: {str(e)}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Create and resolve a match between two registered cards.

        How the match works:
        1. Look up both cards by their IDs
        2. Compare their attack + health (total power)
        3. Higher power wins (simple but clear)
        4. Winner gets +1 win, loser gets +1 loss
        5. Both ratings are recalculated
        6. Health is reset for the next match

        Parameters:
            card1_id (str): ID of the first card
            card2_id (str): ID of the second card

        Returns:
            dict: Match results including winner and new ratings
        """
        try:
            # Look up the cards
            card1: TournamentCard = self.cards.get(card1_id, None)
            card2: TournamentCard = self.cards.get(card2_id, None)

            # Validate both cards exist
            if card1 is None:
                return {"error": f"Card not found: {card1_id}"}
            if card2 is None:
                return {"error": f"Card not found: {card2_id}"}

            # Combat! Each card attacks the other
            card1.attack(card2)
            card2.attack(card1)

            # Determine winner by total power (attack + health)
            card1_power: int = card1.attack_power + card1.health
            card2_power: int = card2.attack_power + card2.health

            if card1_power >= card2_power:
                winner_id: str = card1_id
                loser_id: str = card2_id
                winner_card: TournamentCard = card1
                loser_card: TournamentCard = card2
            else:
                winner_id = card2_id
                loser_id = card1_id
                winner_card = card2
                loser_card = card1

            # Update records
            winner_card.update_wins(1)
            loser_card.update_losses(1)

            # Reset health for next match
            card1.reset_health()
            card2.reset_health()

            # Track total matches
            self.matches_played += 1

            return {
                "winner": winner_id,
                "loser": loser_id,
                "winner_rating": winner_card.rating,
                "loser_rating": loser_card.rating
            }
        except Exception as e:
            return {"error": f"Match failed: {str(e)}"}

    def get_leaderboard(self) -> list:
        """
        Get all cards sorted by rating (highest first).

        Returns:
            list: List of dicts with card ranking info

        """
        try:

            def get_rating(x):
                return x[1].rating

            sorted_cards: list = sorted(
                self.cards.items(),
                key=get_rating,
                reverse=True
            )

            leaderboard: list = []
            for rank, (card_id, card) in enumerate(sorted_cards, 1):
                leaderboard.append({
                    "rank": rank,
                    "card_id": card_id,
                    "name": card.name,
                    "rating": card.rating,
                    "record": f"{card.wins}-{card.losses}"
                })

            return leaderboard
        except Exception as e:
            return [{"error": f"Leaderboard failed: {str(e)}"}]

    def generate_tournament_report(self) -> dict:
        """
        Generate overall tournament statistics.

        Returns:
            dict: Complete tournament report
        """
        try:
            total_cards: int = len(self.cards)

            # Calculate average rating
            avg_rating: int = 0
            if total_cards > 0:
                total_rating: int = sum(
                    card.rating for card in self.cards.values()
                )
                avg_rating = total_rating // total_cards

            return {
                "total_cards": total_cards,
                "matches_played": self.matches_played,
                "avg_rating": avg_rating,
                "platform_status": "active" if total_cards > 0
                else "inactive"
            }
        except Exception as e:
            return {"error": f"Report failed: {str(e)}"}