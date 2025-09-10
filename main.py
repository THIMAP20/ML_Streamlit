import streamlit as st
import pandas as pd
import joblib
import altair as alt

model = joblib.load("predict_new_campaign.pkl")

st.write("""
# My first app
Hello *world!*
""")
