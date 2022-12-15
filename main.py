import streamlit as st

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
    """
    st.info(content)