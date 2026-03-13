from abc import ABC, abstractmethod


class Rankable(ABC):

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate and return the current rating.

        Returns:
            int: The rating number (higher = better)
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Add wins to the record.

        Parameters:
            wins (int): Number of wins to add
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Add losses to the record.

        Parameters:
            losses (int): Number of losses to add
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Get ranking information.

        Returns:
            dict: Ranking details (rating, wins, losses, etc.)
        """
        pass
