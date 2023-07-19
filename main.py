import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/sunny.jpg")
with col2:
    st.title("Mrunal Wankhade")
    content ="""
    Hi, I am Mrunal! I am a Data Analyst.
    """
    st.info(content)