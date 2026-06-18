import re


def is_email(value: str) -> bool:
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value or ""))


def is_required(value: str) -> bool:
    return bool(str(value or "").strip())
