import google.generativeai as genai

# https://aistudio.google.com/app/apikey
from env import GOOGLE_API_KEY

def gemini(user_msg):
    genai.configure(api_key=GOOGLE_API_KEY)

    for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
        print(m.name)

    model = genai.GenerativeModel('gemini-pro')
    #response = model.generate_content("What is the meaning of life?")
    #print(response.text)
    response = model.generate_content(user_msg)
    ai_msg = response.text

    # Speech Analysis
    # print(response.prompt_feedback)
    return ai_msg