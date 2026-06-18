import streamlit as st


def create_task(payload: dict) -> None:
    st.session_state.setdefault("local_data", {}).setdefault("tasks", []).append(payload)
