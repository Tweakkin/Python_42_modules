"""
This module models and validates alien contact reports using Pydantic.
"""

from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    """
    Enum representing the possible types of alien contact.
    """
    radio: str = "radio"
    visual: str = "visual"
    physical: str = "physical"
    telepathic: str = "telepathic"


class AlienContact(BaseModel):
    """
    Represents a single alien contact.
    Validates the structure.
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    # Valid contact
    try:
        contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 6, 15, 22, 30),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
    except Exception as e:
        print(f"Unexpected error: {e}")

    print("======================================")

    # Invalid contact: telepathic with only 1 witness
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 6, 16, 10, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            is_verified=False
        )
    except Exception as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
