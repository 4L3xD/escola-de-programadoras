import google.generativeai as genai
from PIL import Image
from downloadImage import ImageProcessing
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

        # Speech Analysis
        # print(response.prompt_feedback)
        return response.text

    def vision(self):
        img_url = self.user_msg
        img_proc = ImageProcessing(img_url)
        img_name = img_proc.download_img()
        
        img_path = f'./bot/img/{img_name}'
        img = Image.open(img_path)
        # img.show()

        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(img)
        img_proc.delete_image(img_path)

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