from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(Enum):
    """ contact types """
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """ field requirements"""
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_id(self):
        """Contact ID must start with "AC" (Alien Contact)"""
        if self.contact_id.startswith("AC"):
            return self
        else:
            raise ValueError("contact id dosent start with AC")

    @model_validator(mode='after')
    def contact_vaLidator(self):
        """Physical needs to be verified also"""
        if self.contact_type != ContactType.PHYSICAL:
            return self
        elif self.contact_type == ContactType.PHYSICAL and self.is_verified is True:
            return self
        else:
            raise ValueError("contact was not verified")

    @model_validator(mode='after')
    def telephathic_val(self):
        if self.contact_type != ContactType.TELEPATHIC:
            return self
        elif self.contact_type == ContactType.TELEPATHIC and self.witness_count >= 3:
            return self
        else:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        
    @model_validator(mode='after')
    def signal_validator(self):
        """strong signal needs message"""
        if self.signal_strength > 7:
            if self.message_received is None or self.message_received == "":
                raise ValueError("Strong signals (> 7.0) should include received messages")
        return self


def main():
    """Testing the system"""
    print("Alien Contact Log Validation")
    print("========================================\n")
    try:
        print("Valid contact report:")
        valid = AlienContact(
            contact_id="AC08707",
            timestamp=datetime.now(),
            location="planet earth",
            contact_type="physical",
            signal_strength=7.22,
            duration_minutes=66,
            witness_count=2,
            message_received="this is the message",
            is_verified=True)

        print("ID:", valid.contact_id)
        print("Type:", valid.contact_type)
        print("Location:", valid.location)
        print(f"Signal: {valid.signal_strength}/10")
        print(f"Duration: {valid.duration_minutes} minutes")
        print("Witnesses:", valid.witness_count)
        print("Message:", valid.message_received)
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'])

    print("========================================\n")
    try:
        print("Expected validation error:")
        invalid = AlienContact(
            contact_id="AC08707",
            timestamp=datetime.now(),
            location="planet earth",
            contact_type="telepathic",
            signal_strength=7.22,
            duration_minutes=66,
            witness_count=2,
            message_received="this is the message",
            is_verified=True)
        print(invalid)
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
