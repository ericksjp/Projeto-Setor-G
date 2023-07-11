# import requests

# links= [
# 'https://gtahash.ru/cars/super/pfister811.jpg', 
# 'https://gtahash.ru/cars/super/italigtb.jpg', 
# 'https://gtahash.ru/cars/super/penetrator.jpg', 
# 'https://gtahash.ru/cars/super/cheetah.jpg', 
# 'https://gtahash.ru/cars/super/sultanrs.jpg', 
# 'https://gtahash.ru/cars/super/zentorno.jpg', 
# 'https://gtahash.ru/cars/super/prototipo.jpg', 
# 'https://gtahash.ru/cars/super/vigilante.jpg', 
# 'https://gtahash.ru/cars/super/tezeract.jpg', 
# 'https://gtahash.ru/cars/super/sheava.jpg', 
# 'https://gtahash.ru/cars/super/voltic2.jpg', 
# 'https://gtahash.ru/cars/super/infernus.jpg', 
# 'https://gtahash.ru/cars/super/zorrusso.jpg', 
# 'https://gtahash.ru/cars/super/xa21.jpg', 
# 'https://gtahash.ru/cars/super/vacca.jpg', 
# 'https://gtahash.ru/cars/super/cyclone.jpg', 
# 'https://gtahash.ru/cars/super/s80.jpg', 
# 'https://gtahash.ru/cars/super/nero2.jpg', 
# 'https://gtahash.ru/cars/super/scramjet.jpg', 
# 'https://gtahash.ru/cars/super/sc1.jpg', 
# 'https://gtahash.ru/cars/super/osiris.jpg', 
# 'https://gtahash.ru/cars/super/bullet.jpg', 
# 'https://gtahash.ru/cars/super/autarch.jpg', 
# 'https://gtahash.ru/cars/super/visione.jpg', 
# 'https://gtahash.ru/cars/super/nero.jpg', 
# 'https://gtahash.ru/cars/super/voltic.jpg', 
# 'https://gtahash.ru/cars/super/fmj.jpg', 
# 'https://gtahash.ru/cars/super/t20.jpg', 
# 'https://gtahash.ru/cars/super/gp1.jpg', 
# 'https://gtahash.ru/cars/super/krieger.jpg', 
# 'https://gtahash.ru/cars/super/emerus.jpg', 
# 'https://gtahash.ru/cars/super/banshee2.jpg', 
# 'https://gtahash.ru/cars/super/vagner.jpg', 
# 'https://gtahash.ru/cars/super/entityxf.jpg', 
# 'https://gtahash.ru/cars/super/tyrus.jpg', 
# 'https://gtahash.ru/cars/super/tempesta.jpg', 
# 'https://gtahash.ru/cars/super/reaper.jpg', 
# 'https://gtahash.ru/cars/super/italigtb2.jpg', 
# 'https://gtahash.ru/cars/super/adder.jpg', 
# 'https://gtahash.ru/cars/super/le7b.jpg', 
# 'https://gtahash.ru/cars/super/turismor.jpg', 
# 'https://gtahash.ru/cars/super/thrax.jpg', 
# 'https://gtahash.ru/cars/latest_cars/entity2=-2120700196=super.jpg', 
# 'https://gtahash.ru/cars/latest_cars/tyrant=-376434238=super.jpg', 
# 'https://gtahash.ru/cars/latest_cars/taipan=-1134706562=super.jpg', 
# 'https://gtahash.ru/cars/heist/furia.jpg', 
# 'https://gtahash.ru/cars/super/tigon.png', 
# ]

# nomes=[
# 'pfister811.png', 
# 'italigtb.png', 
# 'penetrator.png', 
# 'cheetah.png', 
# 'sultanrs.png', 
# 'zentorno.png', 
# 'prototipo.png', 
# 'vigilante.png', 
# 'tezeract.png', 
# 'sheava.png', 
# 'voltic2.png', 
# 'infernus.png', 
# 'zorrusso.png', 
# 'xa21.png', 
# 'vacca.png', 
# 'cyclone.png', 
# 's80.png', 
# 'nero2.png', 
# 'scramjet.png', 
# 'sc1.png', 
# 'osiris.png', 
# 'bullet.png', 
# 'autarch.png', 
# 'visione.png', 
# 'nero.png', 
# 'voltic.png', 
# 'fmj.png', 
# 't20.png', 
# 'gp1.png', 
# 'krieger.png', 
# 'emerus.png', 
# 'banshee2.png', 
# 'vagner.png', 
# 'entityxf.png', 
# 'tyrus.png', 
# 'tempesta.png', 
# 'reaper.png', 
# 'italigtb2.png', 
# 'adder.png', 
# 'le7b.png', 
# 'turismor.png', 
# 'thrax.png', 
# 'entity2.png', 
# 'tyrant.png', 
# 'taipan.png', 
# 'furia.png', 
# 'tigon.png', 
# ]

import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.gtaall.com/gta-5/vehicles/boats.html'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

images=[]
for i, td in enumerate(soup.find_all('span')):
    texto = td.text.strip('src')
    if texto.isdigit():
        print(texto)

    