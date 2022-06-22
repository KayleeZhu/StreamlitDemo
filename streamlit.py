import pandas as pd

import streamlit as st

sp500 = pd.read_csv("StockData/sp500.csv")
st.header("Portfolio Construction Dashboard")
st.sidebar.button("Run")
# st.dropdown("")

start_date = st.sidebar.date_input("Pick a Start Date")
end_date = st.sidebar.date_input("Pick an End Date")