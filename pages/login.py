import streamlit as st
import pandas as pd
import os
from utils.session import init_session, login_user

# Initialize session
init_session()

st.set_page_config(page_title="Qardio Login", layout="wide")

# --------------------- PAGE CENTERING CSS ---------------------
st.markdown("""
<style>

/* Full page center alignment */
.main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 95vh;
}

/* Card container */


/* Center title */
.login-title {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Emoji bigger */
.login-title span {
    font-size: 32px;
}

/* Input fields */
.stTextInput > div > div > input {
    padding: 14px;
    border-radius: 10px;
}

/* Login button */
.stButton > button {
    width: 100%;
    padding: 12px;
    background: #2ecc71 !important;
    border-radius: 10px;
    color: white !important;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------------------


# ----------- LAYOUT TO CENTER THE COLUMN ----------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown('<h2 class="login-title"><span>🔐</span> Login to Qardio</h2>',
                unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    users_file = "users.csv"

    if st.button("Login"):

        # File does not exist
        if not os.path.exists(users_file):
            st.error("No users found. Redirecting to signup...")
            st.switch_page("pages/signup.py")

        users = pd.read_csv(users_file)

        # Email missing
        if email not in users["email"].values:
            st.warning("No user found with this email. Redirecting to signup...")
            st.switch_page("pages/signup.py")

        # Check credentials
        user_row = users[users["email"] == email].iloc[0]

        if user_row["password"] != password:
            st.error("Incorrect password. Try again.")
        else:
            login_user(email)
            st.success("Login successful! Redirecting...")
            st.switch_page("app.py")

    
