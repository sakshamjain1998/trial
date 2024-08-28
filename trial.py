import streamlit as st
from PIL import Image

# Define the path to your image
image_path = "/logo.png"  # Update this path to your image location

# Load and display the image
def display_image(image_path):
    try:
        image = Image.open(image_path)
        st.image(image, caption='Image from JupyterHub', use_column_width=True)
    except Exception as e:
        st.error(f"Error loading image: {e}")

# Streamlit app layout
st.title("Image Display App")
display_image(image_path)
