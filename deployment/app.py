import streamlit as st
from PIL import Image

hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# Hero section
st.title("Welcome to SwasthAI Web Client")
instructions = """
        Either upload your own image or select from
        the sidebar to get a preconfigured image.
        The image you select or upload will be fed
        through the Deep Neural Network in real-time
        and the output will be displayed to the screen.
        """
st.write(instructions)
file= st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if(file):
    st.subheader("Selected Image")
    st.image(Image.open(file).resize((256, 256)), caption="Uploaded Image")
