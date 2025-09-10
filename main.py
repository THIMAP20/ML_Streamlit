import streamlit as st
import pandas as pd
import joblib
import altair as alt
# ----------------------------
# Load trained model
# ----------------------------
model = joblib.load("predict_new_campaign.pkl")

st.set_page_config(page_title="Predict campaign success", layout="wide")

st.title("📊 Predict campaign success")
st.markdown("Predict success of a campaign based on its settings.")
