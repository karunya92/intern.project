from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    role: str = "EMPLOYEE"
    employee_id: str = ""
    password: str = ""
    phone: str = ""
    department: str = ""
    designation: str = ""
    photo: str = ""
