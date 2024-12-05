import google.generativeai as genai
from io import BytesIO
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
import os

def generate_meme(image, context=None):
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",)

    response = model.generate_content(["Generate a concise and humorous meme caption based on the provided image. Focus solely on the caption without any additional explanations or emoji.\n", image], stream=True,
                                      safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    })
    response.resolve()
    ans = response.text
    return ans
