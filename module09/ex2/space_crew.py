from enum import Enum
from datetime import datetime
from pydantic import BaseModel, ValidationError, Field, model_validator


class Rank(Enum):
    """define the ranks"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """individual crew member"""
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """mission with crew list"""
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def master_validator(self):
        """will validate everything"""
        errors = []
        if not self.mission_id.startswith("M"):
            errors += ["Mission dosent starts with M"]
        valid = 0
        for crew in self.crew:
            if crew.rank == Rank.COMMANDER:
                valid += 1
            elif crew.rank == Rank.CAPTAIN:
                valid += 1
        if valid < 1:
            errors += ["the crew must have at least one Commander or Captain"]
        if self.duration_days > 365:
            experience = sum(member.years_experience >= 5 for member in self.crew)
            if experience / len(self.crew) < 0.5:
                errors += ["for long missions (> 365 days) need half experienced crew (5+ years)"]
        for members in self.crew:
            if members.is_active is False:
                errors += ["All crew members must be active"]

        if errors:
            raise ValueError("\n- ".join(errors))

        return self


def main():
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        print("Valid mission created:")
        valid = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            mission_status="planned",
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=42,
                    specialization="Mission Command",
                    years_experience=12,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=31,
                    specialization="Engineering",
                    years_experience=4,
                    is_active=True,
                ),
            ],
        )

        print("Mission:", valid.mission_name)
        print("ID:", valid.mission_id)
        print("Destination:", valid.destination)
        print(f"Duration: {valid.duration_days} days")
        print(f"Budget: ${valid.budget_millions}M")
        print("Crew size:", len(valid.crew))
        print("Crew members:")
        for member in valid.crew:
            print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])
    print("=========================================")
    try:
        print("Expected validation error:")
        invalid = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Pluto Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            mission_status="planned",
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.OFFICER,
                    age=42,
                    specialization="Mission Command",
                    years_experience=2,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=False,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=31,
                    specialization="Engineering",
                    years_experience=4,
                    is_active=True,
                ),
            ],
        )
        print(invalid)
    except ValidationError as e:
        for e in e.errors():
            print(e['msg'])

    print("=========================================")
    print("Validating missions from generated_data/space_missions.json")
    valid, errors = load_and_validate_missions()
    print(f"Valid missions: {len(valid)}")
    if errors:
        print("Errors:")
        for err in errors:
            print(f"- {err}")
    else:
        print("All missions passed validation.")


if __name__ == "__main__":
    main()
