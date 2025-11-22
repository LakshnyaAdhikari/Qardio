import streamlit as st

st.set_page_config(page_title="Qardio Home", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

h1, h2, h3 {
    font-weight: 700;
}

.hero-box {
    padding: 60px;
    border-radius: 25px;
    background: #f7faff;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 50px;
}

.feature-card {
    padding: 25px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.06);
    text-align: center;
}

.feature-card h3 {
    margin-top: 10px;
}

.button-box a > button {
    width: 180px;
    height: 50px;
    border-radius: 10px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)
# ---------------------------------


# ---------- HERO SECTION ----------
st.markdown("""
<div class="hero-box">
    <h1 style="font-size:45px;">💙 Welcome to <span style="color:#1e88e5;">Qardio</span></h1>
    <h3>Your personal companion for heart health, wellness & prevention.</h3>
    <p>Track symptoms, predict risks using AI, learn remedies, connect with doctors — all in one place.</p>
</div>
""", unsafe_allow_html=True)


# ---------- CTA BUTTONS ----------
colA, colB, colC = st.columns([1,1,1])

with colB:
    st.markdown("""
    <div class="button-box" style="text-align:center;">
        <a href="/login">
            <button style="background:#1abc9c; color:white;">Login</button>
        </a><br><br>
        <a href="/signup">
            <button style="background:white; border:2px solid #1abc9c; color:#1abc9c;">Sign Up</button>
        </a>
    </div>
    """, unsafe_allow_html=True)


# ---------- ABOUT SECTION ----------
st.markdown("""
<h2 style='text-align:center; font-size:34px; font-weight:800; color:#2d3436; margin-top:40px;'>
💡 What is Qardio?
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; font-size:18px; color:#555; line-height:1.6; max-width:850px; margin:auto;'>
Qardio is a smart digital wellness platform that helps you monitor, predict, and improve your heart health.<br>
Our mission is to make preventive heart care simple, accessible, and personalized.
</p>
""", unsafe_allow_html=True)


# ---------- FEATURES GRID ----------
st.markdown("""
<h2 style='text-align:center; font-size:34px; font-weight:800; color:#2d3436; margin-top:60px;'>
⭐ Why Choose Qardio?
</h2>
""", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <h2>🧠 AI Predictions</h2>
        <p>Get instant health risk analysis using machine-learning models.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <h2>📊 History Tracking</h2>
        <p>Track your symptoms and trends with visual graphs and statistics.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <h2>👨‍⚕️ Doctor Connect</h2>
        <p>Schedule appointments and consult specialists online with ease.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------- LOGO ----------

