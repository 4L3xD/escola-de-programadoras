import google.generativeai as genai

# https://aistudio.google.com/app/apikey
from credential import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the meaning of life?")
# print(response.text)

# Speech Analysis
print(response.prompt_feedback)