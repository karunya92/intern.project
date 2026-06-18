import requests
import streamlit as st

from config.config import API_BASE_URL


def login_user(email: str, password: str) -> bool:
    try:
        response = requests.post(
            f"{API_BASE_URL}/auth/login",
            json={"email": email, "password": password},
            timeout=3,
        )
        response.raise_for_status()
        result = response.json()
        st.session_state.auth_token = result.get("token", "")
        st.session_state.user_email = email
        st.session_state.user_role = result.get("role", "")
        return True
    except requests.RequestException:
        return False
