import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=300)

with col2:
    st.title("Nirmol Munvar")
    content = """
    Hi, I am Nirmol! I am a Professor, Design and Verification Engineer, Cloud Architect, Python Programmer and a Teacher.
    I graduated in 2019 with a Masters in Technology and have worked with Shah and Anchor Kutchhi Engineering College as 
    an Assistant Professor. I am willing to Purse a PhD in a Computer Science Domain
    My Area of Interests are 
    RTL Design and Verification, SoC Architecture, Physical Design,
    Cloud Architecture, Server Administration, Enterprise Network Design,
    Data Science, Data Mining, Warehousing, Python Desktop, Web and Game Development   
    """
    st.info(content)

content2 = """
Below you can find some of the Apps and Projects I have Built. Feel free to Contact me!
"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])