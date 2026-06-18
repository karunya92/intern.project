from dataclasses import dataclass


@dataclass
class Leave:
    user_id: int
    leave_type: str
    from_date: str
    to_date: str
    reason: str
    status: str = "Pending"
