import streamlit as st


def apply_leave(payload: dict) -> None:
    st.session_state.setdefault("local_data", {}).setdefault("leaves", []).append(payload)
