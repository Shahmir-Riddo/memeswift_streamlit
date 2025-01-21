import streamlit as st
import time
from PIL import Image
from gemini_api import generate_meme
from utils import add_watermark, apply_top_text, align_text
import io


st.set_page_config(page_title="Memeswift - Meme Generator AI")

st.logo('logo2.png')

with st.form("image"):
        uploaded_image = st.file_uploader("Upload An Image", type=["jpg", "jpeg", "png"])
        submit = st.form_submit_button("Generate Meme")

if submit:
                if uploaded_image is not None:
                        input_image = Image.open(uploaded_image)
                        meme_text = align_text(generate_meme(input_image))
                        output_image = add_watermark(apply_top_text(input_image, meme_text))
                        st.write(meme_text)
                        
                     