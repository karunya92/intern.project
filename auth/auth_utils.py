import hashlib
import secrets

import streamlit as st


def hash_password(password: str, salt: str | None = None) -> str:
    salt = salt or secrets.token_hex(16)
    digest = hashlib.sha256(f"{salt}:{password}".encode("utf-8")).hexdigest()
    return f"{salt}:{digest}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        salt, digest = stored_hash.split(":", 1)
    except ValueError:
        return False
    return hash_password(password, salt).split(":", 1)[1] == digest


def is_logged_in() -> bool:
    return "auth_token" in st.session_state


def logout() -> None:
    st.session_state.clear()
