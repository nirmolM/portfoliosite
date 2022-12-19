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
    My Area of Interests are:
    RTL Design and Verification, SoC Architecture, Physical Design,
    Cloud Architecture, Server Administration, Enterprise Network Design,
    Python Desktop, Web and Game Development,
    Data Mining - Warehousing, Database Management, Machine Learning, Artificial Intelligence  
    """
    st.write(f'<div style="text-align: justify"> {content} </div>', unsafe_allow_html=True)

content2 = """
Below you can find some of the Apps and Projects I have Built. Feel free to Contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns((1.5, 0.5, 1.5))

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

#https://github.com/nirmolM/portfolioapp