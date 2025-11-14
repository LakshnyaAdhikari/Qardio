import streamlit as st
import pandas as pd
import os
from utils.session import init_session, login_user

# Initialize session
init_session()

st.set_page_config(page_title="Qardio Login", layout="wide")

st.title("🔐 Login to Qardio")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

users_file = "users.csv"

if st.button("Login"):

    # If no user file exists → take to signup directly
    if not os.path.exists(users_file):
        st.error("No users found. Redirecting to signup...")
        st.switch_page("pages/signup.py")

    users = pd.read_csv(users_file)

    # Email does not exist
    if email not in users["email"].values:
        st.warning("No user found with this email. Redirecting to signup...")
        st.switch_page("pages/signup.py")

    # Fetch row
    user_row = users[users["email"] == email].iloc[0]

    # Wrong password
    if user_row["password"] != password:
        st.error("Incorrect password. Please try again.")
        st.stop()

    # Login success
    login_user(email)
    st.success("Login successful! Redirecting to Qardio Dashboard...")
    st.switch_page("app.py")
