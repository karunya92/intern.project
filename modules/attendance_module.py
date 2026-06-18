import streamlit as st


def mark_attendance(payload: dict) -> None:
    st.session_state.setdefault("local_data", {}).setdefault("attendance", []).append(payload)
