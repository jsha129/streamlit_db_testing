import pandas as pd
import streamlit as st
import os

st.html(os.listdir('../data'))
df = pd.read_csv('../data/data.csv')
st.dataframe(df)
