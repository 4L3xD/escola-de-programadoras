#curl -o image.jpeg https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQ_Kevbk21QBRy-PgB4kQpS79brbmmEG7m3VOTShAn4PecDU5H5UxrJxE3Dw1JiaG17V88QIol19-3TM2wCHw

import google.generativeai as genai
from PIL import Image

# https://aistudio.google.com/app/apikey
from env import GOOGLE_API_KEY


genai.configure(api_key=GOOGLE_API_KEY)

# path='/home/jinx/Documentos/projects/gemini/image.jpg'
img = Image.open(f'./img/food.jpeg')
# img.show()

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
print(response.text)

# response = model.generate_content(
#         [
#             "Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.",
#             img
#         ],
#         stream=True
#     )
# response.resolve()
# print(response.text)
