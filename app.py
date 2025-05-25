import streamlit as st
import time
from PIL import Image
from gemini_api import generate_meme
from utils import add_watermark, apply_top_text, align_text
import io


st.set_page_config(page_title="Memeswift - Meme Generator AI")

st.logo('logo2.png')

with st.sidebar:
        st.write("**We do not save any pictures or memes clicked by users. All content is processed temporarily and is not stored**")
        st.markdown("""
         <a class="gumroad-button" href="https://ahmedsahmirr.gumroad.com/l/memeswiftdonation" style="display:inline-block;background-color:#f6f6f6;color:#000;text-decoration:none;padding:10px 20px;border-radius:5px;border:1px solid #000;font-size:16px;font-weight:bold;">Donate on Gumroad</a>""", unsafe_allow_html=True)
        st.markdown("Developed by [Riddo](https://github.com/Shahmir-Riddo/)")

with st.form("image"):
        
        img_file_buffer = st.camera_input("Take a Picture")
        uploaded_image = st.file_uploader("Upload An Image", type=["jpg", "jpeg", "png"])
        submit = st.form_submit_button("Generate Meme")

if submit:
                if uploaded_image is not None and img_file_buffer is not None:
                        st.error("You can either upload an image or take a picture, but not both.")
                        img_file_buffer = None


                elif uploaded_image is not None:
                        input_image = Image.open(uploaded_image)
                        generated_meme = generate_meme(input_image)
                        meme_text = align_text(generated_meme)
                        output_image = add_watermark(apply_top_text(input_image, meme_text))
                        st.write(meme_text)
                        st.image(output_image)

                elif img_file_buffer is not None:
                        input_image = Image.open(img_file_buffer)
                        generated_meme = generate_meme(input_image)
                        meme_text = align_text(generated_meme)
                        output_image = add_watermark(apply_top_text(input_image, meme_text))
                        st.write(meme_text)
                        st.image(output_image)

                        img_byte_arr = io.BytesIO()
                        output_image.save(img_byte_arr, format='PNG')
                        img_byte_arr = img_byte_arr.getvalue()
                        st.download_button(
                                label='Download Meme',
                                data=img_byte_arr,
                                file_name = 'memeswift.png',
                                mime = "image/png"
                        )                 

                else:
                
                        
                     st.error("Please upload or take a picture before clickick 'Generate'")
