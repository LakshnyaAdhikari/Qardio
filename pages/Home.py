import streamlit as st
import base64

# --- CONFIG ---
st.set_page_config(page_title="Qardio Home", layout="wide")

# ---------------------------------------------------------
# LOAD LOGO (guaranteed method using base64)
# ---------------------------------------------------------
def load_logo():
    # Placeholder for the actual file loading. 
    try:
        with open("assets/logo.png", "rb") as f:
            data = f.read()
    except FileNotFoundError:
        st.error("Logo file not found. Please ensure 'assets/logo.png' is available.")
        return ""
        
    return base64.b64encode(data).decode()

logo_b64 = load_logo()

# ---------------------------------------------------------
# DARK THEME + UI FIXES (CRITICAL LOGO CSS FIX UPDATED)
# ---------------------------------------------------------
st.markdown(f"""
<style>

/* General Styling */
body {{
    background-color: #0d1117 !important;
}}

h1, h2, h3, p {{
    color: #e8e8e8 !important;
}}

/* ❗ FIX: FORCING LOGO SIZE WITH CSS (150PX) */
#qardio-logo img {{
    width: 150px !important; 
    height: auto !important;
    min-width: 150px !important;
    max-width: 150px !important;
    object-fit: contain;
}}

/* Header Text Style */
.qardio-header-text {{
    font-size: 48px !important; 
    font-weight: 900 !important;
    color: #1e90ff !important;
    white-space: nowrap; 
}}

/* Vertical alignment fix for the image and text */
.st-emotion-cache-1629p8f, .st-emotion-cache-1c5vxtn {{ 
    display: flex;
    align-items: center; 
    padding-top: 0 !important; 
}}

/* Hero Box Styling */
.hero-box {{
    padding: 60px;
    border-radius: 25px;
    background: #161b22;
    border: 1px solid #30363d;
    margin-top: 40px; 
    margin-bottom: 50px;
    text-align: left;
}}

/* Feature Card Styling */
.feature-card {{
    padding: 25px;
    border-radius: 15px;
    background: #1c2128;
    border: 1px solid #30363d;
    text-align: center;
    transition: 0.25s;
    min-height: 150px; /* Ensure cards are uniform height */
}}

.feature-card:hover {{
    transform: translateY(-5px);
    background: #222830;
}}

/* Custom Button Styling */
.custom-btn {{
    padding: 15px 35px;
    font-size: 18px;
    border-radius: 10px;
    text-align: center;
    font-weight: 700;
    width: 250px;
    cursor: pointer;
    display: block; 
    margin: 15px auto; 
    transition: all 0.25s ease;
    text-decoration: none !important; 
}}

.login-btn-styled {{
    background: #1abc9c; 
    color: white !important; 
    border: 2px solid #1abc9c;
    box-shadow: 0px 4px 15px rgba(26, 188, 156, 0.5); 
}}

.login-btn-styled:hover {{
    background: #16a085; 
    box-shadow: 0px 6px 20px rgba(26, 188, 156, 0.6);
    transform: translateY(-2px);
}}

.signup-btn-styled {{
    background: transparent;
    color: #1e90ff !important; 
    border: 2px solid #1e90ff;
}}

.signup-btn-styled:hover {{
    background: rgba(30, 144, 255, 0.15); 
    transform: translateY(-2px);
}}

/* FOOTER STYLING */
.qardio-footer {{
    background-color: #161b22; /* Darker than body, lighter than hero box */
    padding: 40px 0;
    margin-top: 60px;
    border-top: 1px solid #30363d;
}}

.footer-link-group h4 {{
    color: #1e90ff !important;
    margin-bottom: 15px;
    font-size: 18px;
}}

.footer-link-group a {{
    display: block;
    color: #b0b0b0 !important;
    text-decoration: none;
    margin-bottom: 8px;
    font-size: 14px;
    transition: color 0.2s;
}}

.footer-link-group a:hover {{
    color: white !important;
}}

.newsletter-box {{
    padding: 20px;
    border: 1px dashed #30363d;
    border-radius: 10px;
    background: #1c2128;
}}

.newsletter-box input[type="text"], .newsletter-box input[type="email"], .newsletter-box button {{
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 10px;
    border: 1px solid #30363d;
    background: #0d1117;
    color: white;
}}
.newsletter-box button {{
    background: #1abc9c;
    color: white;
    cursor: pointer;
    font-weight: bold;
    border: none;
}}
.newsletter-box button:hover {{
    background: #16a085;
}}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TOP LOGO + TITLE
# ---------------------------------------------------------
col_logo, col_name, col_spacer = st.columns([0.25, 0.5, 5])

with col_logo:
    st.markdown('<div id="qardio-logo" style="width: 150px;">', unsafe_allow_html=True)
    st.image(f"data:image/png;base64,{logo_b64}", use_container_width=True) 
    st.markdown('</div>', unsafe_allow_html=True)

with col_name:
    st.markdown("<span class='qardio-header-text'>Qardio</span>", unsafe_allow_html=True)

st.markdown("---") 

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------
st.markdown("""
<div class="hero-box">
    <h1>💙 Welcome to <span style="color:#1e90ff;">Qardio</span></h1>
    <h3>Your personal companion for heart health, wellness & prevention.</h3>
    <p style='max-width:750px;'>
        Track symptoms, predict risks using AI, learn remedies, connect with doctors — all in one place.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# BUTTONS — LOGIN / SIGN UP
# ---------------------------------------------------------
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.markdown(
        f"""<a href="pages/login.py" target="_self" class="custom-btn login-btn-styled">🔐 Login</a>""",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""<a href="pages/signup.py" target="_self" class="custom-btn signup-btn-styled">📝 Sign Up</a>""",
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# FEATURES
# ---------------------------------------------------------
st.markdown("<h2 style='text-align:center; margin-top: 50px;'>⭐ Why Choose Qardio?</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <h2>🧠 AI Predictions</h2>
        <p>Instant heart disease risk score using ML models.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <h2>📊 History Tracking</h2>
        <p>Visual trends, analytics & improvements.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <h2>👨‍⚕️ Doctor Connect</h2>
        <p>Book appointments & online consultations.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# 1. NEW: HEALTH & COMMUNITY PAGES SECTION
# ---------------------------------------------------------
st.markdown("<h2 style='text-align:center; margin-top: 80px;'>📚 Explore & Connect</h2>", unsafe_allow_html=True)

g1, g2, g3 = st.columns(3)

with g1:
    st.markdown("""
    <div class="feature-card" onclick="window.location.href='pages/health_tips.py';">
        <h3>❤️ Daily Health Tips</h3>
        <p>Expert articles on cardiac wellness, diet, and exercise.</p>
    </div>
    """, unsafe_allow_html=True)

with g2:
    st.markdown("""
    <div class="feature-card" onclick="window.location.href='pages/community.py';">
        <h3>💬 Patient Community</h3>
        <p>Share experiences and get support from other users.</p>
    </div>
    """, unsafe_allow_html=True)

with g3:
    st.markdown("""
    <div class="feature-card" onclick="window.location.href='pages/support.py';">
        <h3>❓ Help & Support</h3>
        <p>FAQs, technical assistance, and contact information.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. NEW: PROFESSIONAL FOOTER (FIXED HTML RENDERING)
# ---------------------------------------------------------
st.markdown('<div class="qardio-footer">', unsafe_allow_html=True)

f1, f2, f3, f4 = st.columns([1.5, 1, 1, 2])

with f1:
    st.markdown("<div class='footer-link-group'>", unsafe_allow_html=True)
    # --- FIX APPLIED HERE ---
    st.markdown("<h4>Qardio</h4>", unsafe_allow_html=True) 
    # --- FIX APPLIED HERE ---
    st.markdown("<p style='font-size: 14px; color: #b0b0b0;'>Your digital heart health companion.</p>", unsafe_allow_html=True)
    # --- FIX APPLIED HERE ---
    st.markdown(f"""
        <p style='font-size: 12px; color: #505050; margin-top: 15px;'>
            © 2025 Qardio Inc. | Privacy Policy | Terms of Service
        </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with f2:
    st.markdown("<div class='footer-link-group'>", unsafe_allow_html=True)
    # --- FIX APPLIED HERE ---
    st.markdown("<h4>App Navigation</h4>", unsafe_allow_html=True)
    st.markdown('<a href="#">Dashboard</a>', unsafe_allow_html=True)
    st.markdown('<a href="pages/tracking.py">Tracking</a>', unsafe_allow_html=True)
    st.markdown('<a href="pages/appointments.py">Appointments</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with f3:
    st.markdown("<div class='footer-link-group'>", unsafe_allow_html=True)
    # --- FIX APPLIED HERE ---
    st.markdown("<h4>Resources</h4>", unsafe_allow_html=True)
    st.markdown('<a href="pages/health_tips.py">Health Tips</a>', unsafe_allow_html=True)
    st.markdown('<a href="pages/community.py">Community</a>', unsafe_allow_html=True)
    st.markdown('<a href="pages/support.py">Contact Support</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with f4:
    # --- FIX APPLIED HERE ---
    st.markdown("<h4>Stay Connected to Good Health</h4>", unsafe_allow_html=True)
    st.markdown("<div class='newsletter-box'>", unsafe_allow_html=True)
    # --- FIX APPLIED HERE ---
    st.markdown('<p style="font-size: 14px; margin-bottom: 10px; color: #e8e8e8;">Receive heart health updates and doctor news.</p>', unsafe_allow_html=True)
    
    st.text_input("First Name", label_visibility="collapsed", key="footer_name", placeholder="First Name")
    st.text_input("Email", label_visibility="collapsed", key="footer_email", placeholder="Email Address")
    
    st.markdown('<button>Subscribe</button>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------