import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Health History")

if not os.path.exists("history.csv"):
    st.info("No history yet. Make predictions first.")
else:
    df = pd.read_csv("history.csv")
    st.write("### Recent Records")
    st.dataframe(df.tail(10))

    st.write("### Trends Over Time")
    fig = px.line(df, x="date", y=["ap_hi","ap_lo","BMI","pulse_pressure"], markers=True)
    st.plotly_chart(fig)

    fig2 = px.line(df, x="date", y="risk", title="Risk Probability Trend", markers=True)
    st.plotly_chart(fig2)
