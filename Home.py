import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/sunny.jpg")
with col2:
    st.title("Mrunal Wankhade")
    content = """
    Hi, I am Mrunal! 
    
    I am a Data Analyst currently.
    
    Newly started working on python programming,this page is one of the result of that,which you are seeing right now! 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in python. Feel free to use and contact me!
"""
st.subheader(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://my-todo-app-ijtdnotqssc.streamlit.app/)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://my-todo-app-ijtdnotqssc.streamlit.app/)")
