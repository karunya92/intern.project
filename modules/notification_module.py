import streamlit as st


def add_notification(message: str) -> None:
    st.session_state.setdefault("notifications", []).append(message)
