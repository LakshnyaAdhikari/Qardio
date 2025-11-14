import streamlit as st
from utils.session import init_session, logout_user
from PIL import Image
import os

# -------------------------------------------------------
# INIT SESSION + LOGIN CHECK
# -------------------------------------------------------
init_session()

if not st.session_state.logged_in:
    st.switch_page("pages/login.py")

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(page_title="Qardio App", layout="wide")

# -------------------------------------------------------
# DARK MODE CSS
# -------------------------------------------------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if st.button("🌓 Toggle Dark Mode", use_container_width=True):
    st.session_state.dark_mode = not st.session_state.dark_mode

dark_css = """
<style>
body {
    background-color: #1a1d21 !important;
    color: #e0e0e0 !important;
}
.sidebar .sidebar-content {
    background-color: #15171b !important;
}
</style>
"""

if st.session_state.dark_mode:
    st.markdown(dark_css, unsafe_allow_html=True)

# -------------------------------------------------------
# TOP BAR PROFILE DROPDOWN
# -------------------------------------------------------
profile_container = st.container()
with profile_container:
    col1, col2 = st.columns([9, 1])
    with col2:
        if st.button("👤", help="Profile Menu"):
            st.session_state.profile_open = not st.session_state.get("profile_open", False)

# Profile dropdown menu
if st.session_state.get("profile_open", False):
    st.markdown(f"""
        <div style="
            position:absolute;
            top:80px;
            right:20px;
            background:#2c2f33;
            color:white;
            padding:15px;
            border-radius:12px;
            width:220px;
            box-shadow:0 4px 20px rgba(0,0,0,0.4);
            z-index:999;">
            
            <p><b>Signed in as:</b><br>{st.session_state.user}</p>
            
            <a style="color:#00c2ff;" href="#">⚙ Account Settings</a><br><br>
            <a style="color:#00c2ff;" href="#">📄 Download Reports</a><br><br>
            <a style="color:#00c2ff;" href="#">🌓 Theme Mode: {'Dark' if st.session_state.dark_mode else 'Light'}</a><br><br>
            
            <button style="
                background:#d72638;
                color:white;
                padding:8px 15px;
                border:none;
                border-radius:8px;
                width:100%;
                cursor:pointer;"
                onclick="window.location.href='pages/login.py'">
                Logout
            </button>
        </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------------
st.sidebar.image("assets/logo.png", width=120)
st.sidebar.title("Qardio Navigation")

st.sidebar.page_link("pages/Home.py", label="🏠 Home")
st.sidebar.page_link("pages/QardioPredict.py", label="🧠 Predict")
st.sidebar.page_link("pages/History.py", label="📊 Health History")
st.sidebar.page_link("pages/Remedies.py", label="🌿 Remedies")
st.sidebar.page_link("pages/Doctors.py", label="👨‍⚕️ Doctors")

# -------------------------------------------------------
# GLOBAL STYLING
# -------------------------------------------------------
st.markdown("""
<style>

[data-testid="stButton"] button {
    border-radius: 12px;
}

input, select, textarea {
    border-radius: 10px !important;
}

div[data-testid="stMetricValue"] {
    color: #d72638 !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# MAIN DASHBOARD CONTENT
# -------------------------------------------------------
st.title("❤️ Welcome to Qardio Dashboard")
st.write("Your personalized heart health assistant.")
