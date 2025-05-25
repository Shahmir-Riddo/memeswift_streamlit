#import google.generativeai as genai
from io import BytesIO
#from google.generativeai.types import HarmCategory, HarmBlockThreshold
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os


def generate_meme(image, context=None):
    
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("API_KEY")
    client = genai.Client(api_key=GOOGLE_API_KEY)

    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=['Generate a concise and humorous meme caption based on the provided image. Focus solely on the caption without any additional explanations or emoji.\n', image]
    )
    
    
   
    
    ans = response.text
    return ans
