"""
This module models and validates space missions and their crew members
using Pydantic.
"""

from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator


class Rank(Enum):
    """
    Enum representing the possible ranks of a crew member.
    """
    cadet: str = "cadet"
    officer: str = "officer"
    lieutenant: str = "lieutenant"
    captain: str = "captain"
    commander: str = "commander"


class CrewMember(BaseModel):
    """
    Represents a single crew member assigned to a space mission.
    Validates personal details, rank, and experience.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Represents a space mission with its crew and operational details.
    Validates mission structure and enforces crew composition rules
    such as leadership requirements and experience.
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        # Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Must have at least one Commander or Captain
        has_leader: bool = any(
            m.rank in (Rank.commander, Rank.captain) for m in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        # Long missions need 50% experienced crew (5+ years)
        if self.duration_days > 365:
            experienced: int = sum(
                1 for m in self.crew if m.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (>365 days) require "
                    "at least 50% experienced crew (5+ years)"
                )

        # All crew members must be active
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    # --- Valid mission ---
    try:
        valid_mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="SC001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=42,
                    specialization="Mission Command",
                    years_experience=20,
                ),
                CrewMember(
                    member_id="JS002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                ),
                CrewMember(
                    member_id="AJ003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=28,
                    specialization="Engineering",
                    years_experience=6,
                ),
            ],
            budget_millions=2500.0,
        )
    except Exception as e:
        print(f"Unexpected error: {e}")

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(
            f"- {member.name} "
            f"({member.rank.value}) - {member.specialization}"
        )

    print("\n=========================================")

    # Invalid mission (no Commander or Captain)
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M9999_BAD",
            mission_name="Doomed Mission",
            destination="Venus",
            launch_date=datetime(2024, 9, 1),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="X001",
                    name="Bob Lee",
                    rank=Rank.cadet,
                    age=20,
                    specialization="Sciences",
                    years_experience=50,
                )
            ],
            budget_millions=100.0,
        )
    except Exception as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
