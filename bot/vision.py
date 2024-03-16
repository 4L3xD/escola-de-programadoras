# https://ai.google.dev/tutorials/python_quickstart
# curl -o image.jpeg https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQ_Kevbk21QBRy-PgB4kQpS79brbmmEG7m3VOTShAn4PecDU5H5UxrJxE3Dw1JiaG17V88QIol19-3TM2wCHw

import google.generativeai as genai
from PIL import Image
from downloadImage import ImageProcessing
# https://aistudio.google.com/app/apikey
from env import GOOGLE_API_KEY

class GeminiVision():
    def __init__(self, url):
        self.img_url = url
        genai.configure(api_key=GOOGLE_API_KEY)

    def ai(self):
        img_name = ImageProcessing(self.img_url).download_img()
        
        img = Image.open(f'./bot/img/{img_name}')
        # img.show()

        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(img)

        return response.text

        # response = model.generate_content(
        #         [
        #             "Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.",
        #             img
        #         ],
        #         stream=True
        #     )
        # response.resolve()
        # print(response.text)

# Execução do script
# url = "https://tm.ibxk.com.br/2023/03/09/09075758840013.jpg"
# print(Gemini(url).ai())