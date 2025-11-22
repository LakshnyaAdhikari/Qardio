import streamlit as st

# Page Title
st.title("🌿 Natural & Medical Remedies for Heart Health")

st.markdown("<br>", unsafe_allow_html=True)

# --- GRADIENT CARD CSS ---
card_style = """
<style>
.card {
    background: linear-gradient(135deg, #2a2d33 0%, #1a1c1f 100%) !important;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 24px;
    border: 1px solid #3a3d42;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.25);
    transition: 0.3s ease;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.35);
}
.card h3 {
    margin-top: 0;
    font-weight: 600;
    letter-spacing: 0.3px;
}
.card p {
    font-size: 15.5px;
    line-height: 1.7;
    color: #f2f2f2;
}
.read-btn {
    color: #70a5ff;
    cursor: pointer;
    font-size: 14px;
    padding-top: 8px;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# Helper function
def read_more_block(key, short_para, long_para):
    if st.session_state.get(key, False):
        st.markdown(f"<p>{long_para}</p>", unsafe_allow_html=True)
        if st.button("Read less ↑", key=key + "_less"):
            st.session_state[key] = False
    else:
        st.markdown(f"<p>{short_para}</p>", unsafe_allow_html=True)
        if st.button("Read more ↓", key=key + "_more"):
            st.session_state[key] = True


# ---------------- AYURVEDIC REMEDIES ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 🔵Ayurvedic Remedies")

short1 = """
Traditional Ayurvedic herbs are often used to support cardiovascular strength and overall heart function. 
Remedies such as Arjuna bark may aid in strengthening the cardiac muscles, while ingredients like garlic 
and cinnamon can help regulate cholesterol levels and improve circulation. Ashwagandha and Giloy are also 
recommended to help manage stress, improve immunity, and stabilize blood pressure.
"""

long1 = """
Traditional Ayurvedic herbs are often used to support cardiovascular strength and overall heart function. Remedies such as 
Arjuna bark may aid in strengthening the cardiac muscles and enhancing the rhythm of cardiac contractions. Garlic and 
cinnamon are known for their potential role in supporting lipid regulation and improving vascular health. Ashwagandha 
is widely used to modulate stress hormones and support mental calmness, which indirectly supports heart health. Giloy 
is recognized for its role in improving immunity and reducing inflammation, contributing to cardiovascular stability 
over time.
"""

read_more_block("ayurveda", short1, long1)
st.markdown("</div>", unsafe_allow_html=True)


# ---------------- MEDICAL LIFESTYLE ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 🔵Medical Lifestyle Recommendations")

short2 = """
Lifestyle interventions play a significant role in long-term heart health. Regular exercise, balanced nutrition, 
and reducing salt, sugar, tobacco, and alcohol intake help reduce cardiovascular strain. Maintaining a healthy 
weight and monitoring blood pressure enables early detection of changes. Incorporating meditation or yoga helps 
improve stress management and overall cardiovascular functioning.
"""

long2 = """
Lifestyle interventions play a significant role in long-term heart health. Regular exercise improves heart efficiency, 
lowers resting blood pressure, and stabilizes oxygen delivery. Balanced nutrition reduces inflammation, supports 
metabolism, and maintains lipid levels. Reducing salt, sugar, tobacco, and alcohol intake greatly lowers chronic 
cardiac strain. Consistent monitoring of blood pressure and cholesterol enables early identification of risk factors. 
Incorporating meditation, breathing techniques, or yoga helps regulate the autonomic nervous system, improving stress 
response and cardiovascular stability.
"""

read_more_block("lifestyle", short2, long2)
st.markdown("</div>", unsafe_allow_html=True)


# ---------------- GENERAL HEART CARE ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 🔵General Heart-Care Practices")

short3 = """
Healthy daily habits contribute greatly to optimal heart function. Adequate sleep supports recovery, and proper 
hydration helps maintain healthy blood circulation. Regular walking improves blood flow, while managing emotional 
stress helps reduce unnecessary cardiac strain. Together, these practices foster long-term heart wellness.
"""

long3 = """
Healthy daily habits contribute greatly to optimal heart function. Adequate sleep regulates hormone cycles and promotes 
cardiovascular recovery. Hydration maintains optimal blood viscosity and supports circulation. Regular walking improves 
vascular tone, enhances oxygen delivery, and reduces stiffness in arteries. Stress management techniques such as 
mindfulness, journaling, or breathing practices help reduce stress hormones that put extra pressure on the heart. Over 
time, these habits form a sustainable foundation for long-term cardiac wellness.
"""

read_more_block("care", short3, long3)
st.markdown("</div>", unsafe_allow_html=True)


st.success("These recommendations support overall cardiac wellness. For personalized guidance, consult a healthcare professional.")
