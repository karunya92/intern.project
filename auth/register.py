from modules.user_module import create_user


def register_user(payload: dict) -> tuple[bool, str]:
    if not payload.get("email") or not payload.get("name"):
        return False, "Name and email are required."
    create_user(payload)
    return True, "User registered."
