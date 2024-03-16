# https://ai.google.dev/tutorials/python_quickstart
# curl -o image.jpeg https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQ_Kevbk21QBRy-PgB4kQpS79brbmmEG7m3VOTShAn4PecDU5H5UxrJxE3Dw1JiaG17V88QIol19-3TM2wCHw

import google.generativeai as genai
from PIL import Image
from downloadImage import ImageProcessing
# https://aistudio.google.com/app/apikey
from env import GOOGLE_API_KEY

class Gemini():
    def __init__(self, user_msg):
        self.user_msg = user_msg
        genai.configure(api_key=GOOGLE_API_KEY)

    def nlp(self):
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

        model = genai.GenerativeModel('gemini-pro')
        #response = model.generate_content("What is the meaning of life?")
        #print(response.text)
        response = model.generate_content(self.user_msg)
        ai_msg = response.text

        # Speech Analysis
        # print(response.prompt_feedback)
        return ai_msg

    def vision(self):
        img_url = self.user_msg
        img_name = ImageProcessing(img_url).download_img()
        
        img = Image.open(f'./bot/img/{img_name}')
        # img.show()

        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(img)

        # response = model.generate_content(
        #         [
        #             "Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.",
        #             img
        #         ],
        #         stream=True
        #     )
        # response.resolve()
        # print(response.text)
        return response.text

# Execução do script
# url = "https://tm.ibxk.com.br/2023/03/09/09075758840013.jpg"
# print(Gemini(url).ai())