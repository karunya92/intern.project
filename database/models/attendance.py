from dataclasses import dataclass


@dataclass
class Attendance:
    user_id: int
    attendance_date: str
    status: str
