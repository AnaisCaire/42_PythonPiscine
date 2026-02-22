from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


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
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main():
    """ Testing the validation class"""
    print("Space Station Data Validation")
    print("========================================\n")
    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
<<<<<<< HEAD
        "last_maintenance": datetime.now()
=======
        "last_maintenance": datetime.now(),
        "notes": "this is the test "
>>>>>>> refs/remotes/origin/main
    }
    try:
        valid = SpaceStation(**valid_data)
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size}")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        # print("Last maintenance",
        #      valid.last_maintenance.strftime("%Y-%m-%d %H:%M"))
        if valid.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: Not operational")
    except ValidationError as e:
        for error_message in e.errors():
            print(error_message["msg"])

    print("========================================\n")
    print("Expected validation error:")
    invalid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 25,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime.now(),
        "notes": "this is the test "
    }
    try:
        invalid_data = SpaceStation(**invalid_data)
    except ValidationError as e:
        for error_message in e.errors():
            print(error_message['msg'])


if __name__ == "__main__":
    main()
