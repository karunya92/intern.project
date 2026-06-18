from dataclasses import dataclass


@dataclass
class Skill:
    user_id: int
    skill_name: str
    skill_level: str
