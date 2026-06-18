from dataclasses import dataclass


@dataclass
class Note:
    title: str
    description: str
    created_at: str = ""
    attachment: str = ""
