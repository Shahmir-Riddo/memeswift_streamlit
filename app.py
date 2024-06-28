import streamlit as st
from PIL import Image, ImageDraw, ImageFont 
import google.generativeai as genai
from io import BytesIO
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from utils import align_text, apply_top_text
#import streamlit_shadcn_ui as ui


def generate_meme(image, context=None):
    GOOGLE_API_KEY = "AIzaSyDVkDT2hRx_9e5N1UzJPq6yE73Az_ADAhM"

    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel(
    model_name="gemini-1.0-pro-vision-latest",)

    response = model.generate_content(["Just generate funny meme caption based on the provided image without any extra text.\n", image], stream=True,
                                      safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    })
    response.resolve()
    ans = response.text
    return ans





def main():
    st.title("Memeswift")
    choice = st.radio("Select Image Source: ", ("Upload An Image", "Use Camera"))
    
    if choice == "Use Camera":
        uploaded_file = st.camera_input("Capture an Image")
        image = Image.open(BytesIO(uploaded_file.getvalue()))
        st.image(image, caption="Uploaded Image")
    else:
        uploaded_file = st.file_uploader("Upload a Image")
        if uploaded_file is not None:
            image = Image.open(BytesIO(uploaded_file.getvalue()))
            
            st.image(image, caption="Uploaded Image")

    
    if st.button("Generate Meme"):
        caption = generate_meme(image)
        image = Image.open(BytesIO(uploaded_file.getvalue()))
        meme = apply_top_text(image, caption)
        st.image(meme, caption="Generated Meme - ")
        st.write(caption)






if __name__ == "__main__":
    main()