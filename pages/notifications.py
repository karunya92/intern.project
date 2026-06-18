import streamlit as st

import app


app.page_config()
app.init_state()
st.title("Notifications")
notifications = st.session_state.get("notifications", [])
if notifications:
    for message in notifications:
        st.info(message)
else:
    st.info("No notifications yet.")
