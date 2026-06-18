from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str = ""
    priority: str = "Medium"
    status: str = "Not Started"
    deadline: str = ""
    assigned_to: int = 0
