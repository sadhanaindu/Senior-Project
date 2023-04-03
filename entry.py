import streamlit as st

st.set_page_config(
    page_title="entry"
)

st.write("# Facial Emotion Recognition! 👋")

st.sidebar.success("Select whether you want to detect yourself, detect emotion, or take photos to improve our algorithm.")

st.markdown(
    """
   Select whether you want to take an exam using facial detection or take photos to improve our algorithm
   in the side bar on your left. 
"""
)