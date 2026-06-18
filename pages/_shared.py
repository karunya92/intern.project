import streamlit as st

import app


def render_page(page_func) -> None:
    app.page_config()
    app.init_state()
    if "auth_token" not in st.session_state:
        app.login()
        return
    page_func()
