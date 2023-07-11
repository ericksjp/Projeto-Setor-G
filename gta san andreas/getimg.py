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
url = 'https://www.gtabase.com/gta-san-andreas/characters/'

# Faz a requisição da página
r = requests.get(url)

# print(r)

# Transforma o conteúdo em um objeto BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

titulos=[]
for i, td in enumerate(soup.find_all (class_ = 'roster')):
    title = td.get('title')
    for w,tc in enumerate(td.find_all('img')):
        te = 'https://www.gtabase.com/'+tc['src']
        # if "z4=" not in te:
        #     response = requests.get(te)
        #     with open(f'assets/img{i}.png', 'wb') as f:
        #         f.write(response.content)
        title = tc.get('title')
        titulos.append(title)
        
i = 0
while (i<=46):
    with open(f'personagens.txt', 'a') as f:
        f.write(f'''
        <div class="roster">
            <img src="assets/img{i}.png" alt="{titulos[i]}" title="{titulos[i]}" class="item-image-fulltext jch-lazyloaded" width=100px; height=100px;>
            <div class="roster_name">{titulos[i]}</div>
        </div>  ''')
    i+=1

#     if src.startswith('/'):
#         src = 'https://gtahash.ru' + src
        
#     print(f"'{src}', ")
    
# for i in lista:
#     print(i)
    

