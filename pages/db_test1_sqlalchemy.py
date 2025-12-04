import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Replace with your Neon PostgreSQL credentials
HOST = "ep-icy-dawn-a7q2fmwh-pooler.ap-southeast-2.aws.neon.tech"
USER = "neondb_owner"
PASSWORD = "npg_2zsJAF3pECPo"
DATABASE = "neondb"
PORT = 5432

# SQLAlchemy connection using pg8000 instead of psycopg2
connection_string = (
    f"postgresql://{user}:{password}@{host}:{port}/{database}"
)

engine = create_engine(connection_string)

# SQL query
query = "SELECT * FROM home LIMIT 10;"

# Fetch data
try:
    df = pd.read_sql(query, engine)
    st.success("Connected to Neon + fetched data successfully!")
    st.dataframe(df)        # Streamlit dataframe
    # or: st.table(df)      # Static table
except Exception as e:
    st.error(f"Query failed: {e}")
