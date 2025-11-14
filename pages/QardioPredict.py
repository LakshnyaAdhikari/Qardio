import streamlit as st
import pandas as pd
import joblib
import datetime
import os
from utils.pdf_generator import generate_pdf

st.title("🧠 QardioPredict – Heart Risk Analysis")
st.write("Enter your details below and let Qardio analyze your heart health using AI.")

model = joblib.load("model/model.pkl")

# --- FORM UI ---
with st.form("predict_form", clear_on_submit=False):

    st.subheader("🩺 Patient Health Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=30)
        height = st.number_input("Height (cm)", min_value=90, max_value=210, value=170)
        weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=60)

    with col2:
        ap_hi = st.number_input("Systolic BP (ap_hi)", min_value=80, max_value=240, value=120)
        ap_lo = st.number_input("Diastolic BP (ap_lo)", min_value=40, max_value=140, value=80)
        cholesterol = st.selectbox("Cholesterol Level", [1, 2, 3])

    with col3:
        gluc = st.selectbox("Glucose Level", [1, 2, 3])
        smoke = st.selectbox("Do you smoke?", [0, 1])
        alco = st.selectbox("Alcohol intake?", [0, 1])
        gender = st.selectbox("Gender (1=Female, 2=Male)", [1, 2])
        active = st.selectbox("Active Lifestyle (1=Yes, 0=No)", [1, 0])

    submitted = st.form_submit_button("🔍 Predict")

# ---- PREDICTION LOGIC ----
if submitted:

    BMI = weight / ((height / 100) ** 2)
    pulse_pressure = ap_hi - ap_lo

    input_df = pd.DataFrame([[
        age, ap_hi, ap_lo, weight, height,
        cholesterol, gluc, smoke, alco, gender, active,
        BMI, pulse_pressure
    ]], columns=[
        "age","ap_hi","ap_lo","weight","height",
        "cholesterol","gluc","smoke","alco","gender","active",
        "BMI","pulse_pressure"
    ])

    prediction = model.predict(input_df)[0]
    risk = model.predict_proba(input_df)[0][1] * 100

    # --- RESULT CARD ---
    st.markdown("---")
    st.subheader("📌 Qardio AI Result")

    if prediction == 1:
        st.error(f"❤️ HIGH RISK DETECTED\nRisk Probability: **{risk:.2f}%**")
    else:
        st.success(f"💚 LOW RISK\nRisk Probability: **{risk:.2f}%**")

    # ---- SAVE HISTORY ----
    entry = input_df.copy()
    entry["risk"] = risk
    entry["result"] = prediction
    entry["date"] = datetime.date.today()

    if not os.path.exists("history.csv"):
        entry.to_csv("history.csv", index=False)
    else:
        entry.to_csv("history.csv", mode="a", index=False, header=False)

    # ---- PDF DOWNLOAD BUTTON ----
    st.markdown("### 📄 Download Detailed PDF Report")

    report_data = {
        "Age": age,
        "Height": height,
        "Weight": weight,
        "BMI": round(BMI, 2),
        "Systolic BP": ap_hi,
        "Diastolic BP": ap_lo,
        "Pulse Pressure": pulse_pressure,
        "Cholesterol": cholesterol,
        "Glucose": gluc,
        "Smoke": smoke,
        "Alcohol": alco,
        "Gender": gender,
        "Active": active,
    }

    filename = generate_pdf(
        result="High Risk" if prediction == 1 else "Low Risk",
        probability=risk,
        user_data=report_data,
        filename="Qardio_Report.pdf"
    )

    with open(filename, "rb") as f:
        st.download_button("⬇ Download PDF Report", f, file_name="Qardio_Report.pdf")
