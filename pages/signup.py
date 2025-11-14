import streamlit as st
import pandas as pd
import os
from utils.session import init_session

init_session()

st.set_page_config(page_title="Qardio - Sign Up", layout="wide")

st.title("📝 Create Your Qardio Account")

email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

users_file = "users.csv"

def save_user(email, password):
    df = pd.DataFrame([[email, password]], columns=["email", "password"])
    if not os.path.exists(users_file):
        df.to_csv(users_file, index=False)
    else:
        df.to_csv(users_file, mode="a", header=False, index=False)

if st.button("Sign Up"):

    # Password mismatch
    if password != confirm:
        st.error("Passwords do not match")
        st.stop()

    # If users file exists → check duplicate email
    if os.path.exists(users_file):
        users = pd.read_csv(users_file)

        if email in users["email"].values:
            st.error("User already exists. Redirecting to login...")
            st.switch_page("pages/login.py")

    # Save new user
    save_user(email, password)
    st.success("Account created successfully! Redirecting to Login...")

    st.switch_page("pages/login.py")
