import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SwasthAI: AI-Powered Health Diagnosis", 
    page_icon="https://i.postimg.cc/zfjkwzPq/swasth-AILogo.png", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.title('Scan')
instructions = """
        Either upload your own image or select from
        the sidebar to get a preconfigured image.
        The image you select or upload will be fed
        through the Deep Neural Network in real-time
        and the output will be displayed to the screen.
        """
st.write(instructions)
selected_option=""

st.sidebar.title("Scan Options")
dropdown_options = ["Lungs", "Brain"]

st.subheader("Image Upload")
file= st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if(file):
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(file).resize((256, 256)))
        with col2:
                selected_option = st.selectbox("Select Domain Model:", dropdown_options, index=None, placeholder="Unselected", help="Used for selecting the domain model to be used for scanning the image.")
                st.button("Scan", "https://docs.streamlit.io/library/api-reference/widgets/st.button")

st.subheader("Results")
