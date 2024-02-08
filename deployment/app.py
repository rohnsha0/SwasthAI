import base64
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SwasthAI: AI-Powered Health Diagnosis", 
    page_icon="https://i.postimg.cc/zfjkwzPq/swasth-AILogo.png", 
    layout="wide", 
    initial_sidebar_state="expanded")

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

# Sidebar
st.sidebar.title("Scan Options")
dropdown_options = ["Lungs", "Brain"]
with st.sidebar:
    selected_option = st.selectbox("Select Domain Model:", dropdown_options, index=None, placeholder="Unselected", help="Used for selecting the domain model to be used for scanning the image.")
if selected_option == "Lungs":
    st.write("You selected Lungs!")
elif selected_option == "Brain":
    st.write("You selected Brain!")
else:
    st.write("Selecct a cateogory to proceed!")

