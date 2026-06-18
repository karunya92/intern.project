import streamlit as st


def add_skill(payload: dict) -> None:
    st.session_state.setdefault("local_data", {}).setdefault("skills", []).append(payload)
