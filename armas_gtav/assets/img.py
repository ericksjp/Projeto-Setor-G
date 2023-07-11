import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By

# cria uma instância do navegador
driver = webdriver.Chrome()

# navega até a página desejada
driver.get('https://wiki.rage.mp/index.php?title=Vehicles#Commercials')

# encontra todos os elementos 'img' na página
imgs = driver.find_elements(By.TAG_NAME, 'img')

# cria um diretório para salvar as imagens
# if not os.path.exists('images'):
#     os.mkdir('images')

# itera sobre todos os elementos 'img', baixa as imagens e salva no diretório criado
for i, img in enumerate(imgs):
    src = img.get_attribute('src')
    print(src)

# fecha o navegador
driver.quit()