import streamlit as st
import base64
from PIL import Image

st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1")
st.markdown("""
1. Muhammad Faqih Jundullah
2. Lintang Kasyfi            
""")
st.write("Displaying an Images")
st.image("c:/pemandangan.jpg")
st.write("Image Courtesy: pngtree.com")

st.write("Displaying Multiple Images")
animal_images = [
    'c:/elang.png',
    'c:/gajah.png',
    'c:/jerapah.png',
    'c:/singa.png',
]
st.image(animal_images, width=150)
st.write("Image Courtesy: pngtree")

def add_local_backgound_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Background Image")
# Calling Image in function
add_local_backgound_image_('c:/gajah.png')

original_image = Image.open("c:/singa.png")
# Display Original Image
st.title("Original Image")
st. image(original_image)
# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
#Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)