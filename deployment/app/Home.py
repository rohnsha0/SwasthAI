import base64
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SwasthAI: AI-Powered Health Diagnosis", 
    page_icon="https://i.postimg.cc/zfjkwzPq/swasth-AILogo.png", 
    layout="centered", 
    initial_sidebar_state="collapsed")

hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# Hero section
st.title("About Project SwasthAI")
instructions = """
        Either upload your own image or select from
        the sidebar to get a preconfigured image.
        The image you select or upload will be fed
        through the Deep Neural Network in real-time
        and the output will be displayed to the screen.
        """
st.write(instructions)

st.button("Get Started", "https://docs.streamlit.io/library/api-reference/widgets/st.button")

