from datetime import datetime
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    """
    data structure validation class
    """
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(..., default=True)
    notes: str = Field(..., max_length=200)


def main():
    """ Testing the validation class"""
    print("Space Station Data Validation")
    print("========================================")
    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3
    }
    valid = SpaceStation(**valid_data)
    print(f"the data is: {valid.items}")


if __name__ == "__main__":
    main()
