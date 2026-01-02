import pandas as pd
import streamlit as st

df = pd.read_csv('/data/data.csv')
st.dataframe(df)
