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
            raise ValueError("[Error] contact id dosent start with AC")


def main():
    """Testing the system"""
    try:
        test = AlienContact(contact_id="AC008707",
                            timestamp=datetime.now(),
                            location="planet earth",
                            contact_type="visual",
                            signal_strength=6.22,
                            duration_minutes=66,
                            witness_count=32,
                            message_received="this is the message",
                            is_verified=True
                            )
        # test1 = AlienContact(contact_id="008707", contact_type=ContactType.RADIO)
        print(test)
        # print(test1)
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
