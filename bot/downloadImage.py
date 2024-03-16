import requests
import os
from env import PATH 

class ImageProcessing():
    def __init__(self, url):
        self.img_url = url 
        ext = url.split(".")[-1]
        img_db = os.listdir(PATH)
        
        if len(img_db) == 0:
            self.img_name = f"img_0.{ext}"
        else:
            img_number = img_db[-1].split("_")[1].split(".")[0]
            self.img_name = f"img_{int(img_number) + 1}.{ext}" 
    
    def download_img(self):
        response = requests.get(self.img_url)

        if response.status_code == 200:
            with open(f"{PATH}/{self.img_name}", 'wb') as f:
                f.write(response.content)
            print("Download concluído: ", self.img_name)
        else:
            print("Falha ao fazer o download: ", response.status_code)

        return self.img_name