import requests
import os
from env import path 

class ImageProcessing():
    def __init__(self, url):
        self.img_url = url 
        ext = url.split(".")[-1]
        img_db = os.listdir(path)
        
        if len(img_db) == 0:
            self.img_name = f"img_0.{ext}"
        else:
            img_number = img_db[-1].split("_")[1].split(".")[0]
            self.img_name = f"img_{int(img_number) + 1}.{ext}" 
        
        return self.download_img()
    
    def download_img(self):
        response = requests.get(self.img_url)

        if response.status_code == 200:
            with open(f"{path}/{self.img_name}", 'wb') as f:
                f.write(response.content)
            print("Download concluído: ", self.img_name)
        else:
            print("Falha ao fazer o download: ", response.status_code)

# Teste hardcoded do script
url = "https://tm.ibxk.com.br/2023/03/09/09075758840013.jpg"
ImageProcessing(url)