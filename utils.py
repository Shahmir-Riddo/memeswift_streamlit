from PIL import Image, ImageDraw, ImageFont 
import os
import streamlit as st

def logo():
    st.logo("logo2.png", size="large", icon_image="logo.png")

def align_text(text):

    words = text.split()
    aligned_text = ""

    for index, word in enumerate(words, start=1):
        aligned_text += word
        if index % 6 == 0:
            aligned_text += "\n"
        else:
            aligned_text += " "

    return str(aligned_text.strip())



def apply_top_text(img, text):

    text = text.upper()
    base_app_directory = os.path.dirname(os.path.abspath(__file__))
    font_filename = 'impact.ttf'
    font_path = os.path.join(base_app_directory, font_filename)
    image = img.resize((960, 960))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, 57)

    text = align_text(text)
    text_size = draw.textbbox((0,0), text, font=font)
    _, _, text_width, text_length = text_size
    
    print(text)
    x = (image.width - text_width) // 2
    y = 10
    
    draw.text((x, y), f"{text}", font=font, fill=(255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0)) # Change the text and position as desired

        
    return image


def add_watermark(img):

    text = "Made with Memeswift"
    base_app_directory = os.path.dirname(os.path.abspath(__file__))
    font_filename = 'impact.ttf'
    font_path = os.path.join(base_app_directory, font_filename)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 15)

    text = align_text(text)
    text_size = draw.textbbox((0,0), text, font=font)
        
    _, _, text_width, text_height = text_size

    position = (img.size[0] - text_width - 10, img.size[1] - text_height - 10)
    
    draw.text(position, f"{text}", font=font, fill=(255, 255, 255)) # Change the text and position as desired

        
    return img