import pandas as pd
import streamlit as st
import os

st.html(os.listdir(os.getcwd()))
df = pd.read_csv('data/data.csv')
st.dataframe(df)
