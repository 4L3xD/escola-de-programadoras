import requests
import os
from env import PATH 

class ImageProcessing():
    def __init__(self, url):
        self.img_url = url 
        ext = url.split(".")[-1]
        img_db = os.listdir(PATH)
        
        if len(img_db) != 0:
            for image in img_db:
                self.delete_image(image)
        
        self.img_name = f"img_0.{ext}"
        
    def delete_image(self, filename):
        try:
            os.remove(filename)
            print(f"Imagem {filename} deletada com sucesso!")
        except FileNotFoundError:
            print(f"Imagem {filename} não encontrada.")
        except Exception as e:
            print(f"Ocorreu um erro ao deletar a imagem: {e}")
    
    def download_img(self):
        response = requests.get(self.img_url)

        if response.status_code == 200:
            with open(f"{PATH}/{self.img_name}", 'wb') as f:
                f.write(response.content)
            print("Download concluído: ", self.img_name)
        else:
            print("Falha ao fazer o download: ", response.status_code)

        return self.img_name