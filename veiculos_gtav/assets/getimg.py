# import os
# import urllib.request
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get('https://gtahash.ru/car/?c=super')

# imgs = driver.find_elements(By.TAG_NAME, 'img')

# if not os.path.exists('images'):
#     os.mkdir('images')

# for i, img in enumerate(imgs):
#     src = img.get_attribute('src')
#     if src:
#         urllib.request.urlretrieve(src, f'images/image{i}.png')
# driver.quit()
import requests
from bs4 import BeautifulSoup
import os

# Cria uma pasta para salvar as imagens
# if not os.path.exists('images'):
#     os.mkdir('images')

# URL do site com os carros super
url = 'https://gtahash.ru/car/?c=super'

# Faz a requisição da página
r = requests.get(url)

# Transforma o conteúdo em um objeto BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

num = 1
lista=[]
for i in range(50):
    lista.append(num)
    num += 4
# Procura pelas tags de imagem e baixa cada uma
for i, td in enumerate(soup.find_all('td')):
    if i in lista:
        texto = td.text.strip() # pega apenas o texto do elemento e remove espaços em branco
        print(f"'{texto}.png', ")

        
    

#     if src.startswith('/'):
#         src = 'https://gtahash.ru' + src
        
#     print(f"'{src}', ")
    
# for i in lista:
#     print(i)
    

