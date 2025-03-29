import streamlit as st
import awswrangler as wr

df = wr.s3.read_csv("s3://sumant28-testinguploads/workout_data.csv")

st.header("trying")

st.dataframe(df.head())