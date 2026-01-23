# from PIL import ImageFont
import os

font_path = r"D:\DTL_Study_Companion2\static\fonts\handwriting.ttf"

print("Exists:", os.path.exists(font_path))

font = ImageFont.truetype(font_path, 28)

print("FONT LOADED SUCCESSFULLY")
