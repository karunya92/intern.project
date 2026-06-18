import streamlit as st


def create_user(payload: dict) -> None:
    st.session_state.setdefault("local_data", {}).setdefault("employees", []).append(payload)


def list_users() -> list[dict]:
    return st.session_state.setdefault("local_data", {}).setdefault("employees", [])
