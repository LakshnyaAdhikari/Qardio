import streamlit as st

st.title("👨‍⚕️ Doctor Directory")

st.subheader("Recommended Cardiologists")

st.info("Dr. Rohan Kapoor – Fortis Hospital – 10 yrs experience")
if st.button("Book Dr. Rohan"):
    st.success("Appointment request sent.")

st.info("Dr. Meera Iyer – Apollo Hospital – 8 yrs experience")
if st.button("Book Dr. Meera"):
    st.success("Appointment request sent.")
