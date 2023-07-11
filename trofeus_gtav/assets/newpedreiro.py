import requests
from bs4 import BeautifulSoup
import os

# url = input("Informe a ulr do site -> ")
# diretorio = input("Informe onde as Imagens serão guardadas-> ")
# classe = input ("Informe qual a classe de veiculos: ")
# descricao = input ("Faça uma descrião para essa classe: ")


r = requests.get("https://psxbrasil.com.br/trophy-guide/trophy-guide-grand-theft-auto-v/")

# Transforma o conteúdo em um objeto BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

div = soup.find(id='lista-trofeus')

lista=[]
for t in div.find_all('div', attrs={'class': 'trofeu-montado'}):
        lista.append(t)
        

# imgs = []
# imagens = div.find_all('img')
# for qqq,imagem in enumerate(imagens):
#     if imagem.has_attr('src'):
#         source = imagem['src']
#         if "png" in source and "images" not in source and "https://psxbrasil.com.br/trophyguide/h.png" not in source and "gta" in source:
#             imgs.append(source)

# imgs2=[]
# for i,z in enumerate(imgs):
#     if i<=5:
#         imgs2.append(z)
#         print(z)

# rating = []
# imagens = div.find_all('img')
# for qqq,imagem in enumerate(imagens):
#     if imagem.has_attr('src'):
#         source = imagem['src']
#         if "png" in source and "images" not in source and "https://psxbrasil.com.br/trophyguide/h.png" not in source and "gta" not in source and "bug" not in source and "https://psxbrasil.com.br/trophyguide/m.png" not in source:
#             rating.append(source)

# rating2=[]
# for i,z in enumerate(rating):
#     if i>5:
#         if z=="https://psxbrasil.com.br/trophyguide/b.png":
#             rating2.append("Bronze")
#         if z=="https://psxbrasil.com.br/trophyguide/g.png":
#             rating2.append("Ouro")
#         if z=="https://psxbrasil.com.br/trophyguide/s.png":
#             rating2.append("Prata")

# nomes = []
# for i,t in enumerate(lista):
#     for g in t.find('b'):
#         print(g)
#         nomes.append(g.text)

# descricoes = []
# for q,o in enumerate(lista):
#     if (q>5):
#         oo = 0
#         for k in o.find('p'):
#             if (k.text!=""):
#                 if (oo==0):
#                     descricoes.append(k.text)
#                 oo+=1
                    
textos = []
for a in div.find_all('b'):
    texto = a.text
    if "DLC: GTA ONLINE HEISTS" not in texto:
        # print(texto[4:])
        textos.append(texto[4:])
        
for w in range(59):
    with open(f'dd.txt', 'a', encoding="utf-8") as f:
        f.write(f"""
            <li><a href="#trofeu{w+1}"><span>3.{w+1}</span> {textos[w]}</a></li>""")
    
# print(div)

# for w in range(53):
#     print(f"{textos[w]}")
     
    
# if not os.path.exists(f'images/{diretorio}'):
#     os.mkdir(f'images/{diretorio}')


# c=1
# for i in imgs2:
#     response = requests.get(i)

#     with open(f'assets/images/img{c}.png', 'wb') as f:
#         f.write(response.content)
#     c+=1

# for w in range(53):
#     with open(f'trofeu.txt', 'a', encoding="utf-8") as f:
#         f.write(f"""
#         <div class="grid-container">
#             <img src="./assets/images/img{w+7}.png" alt="" class="grid-item image">
#             <b class="grid-item b-text"> <span class="indice">{w+7}</span>. {textos[w]}</b> <br>""")

#     if (rating2[w]== "Bronze"):
#         with open(f'trofeu.txt', 'a', encoding="utf-8") as f:
#             f.write(f"""
#             <p class="grid-item i-text"><img class="trophyimg" src="./assets/trophys/bronze.png" alt=""> Bronze</p>
#             <p class="gri-item d-text">{descricoes[w]}</p>
#         </div>
#             """)
#     elif (rating2[w]=="Prata"):
#             with open(f'trofeu.txt', 'a', encoding="utf-8") as f:
#                 f.write(f"""
#                 <p class="grid-item i-text"><img class="trophyimg" src="./assets/trophys/silver.png" alt=""> Prata</p>
#                 <p class="gri-item d-text">{descricoes[w]}</p>
#             </div>
#                 """)
#     elif (rating2[w]=="Ouro"):
#         with open(f'trofeu.txt', 'a', encoding="utf-8") as f:
#             f.write(f"""
#             <p class="grid-item i-text"><img class="trophyimg" src="./assets/trophys/gold.png" alt=""> Ouro</p>
#             <p class="gri-item d-text">{descricoes[w]}</p>
#         </div>
#             """)

# with open(f'{classe}.txt', 'a') as f:
#     f.write("""
#             </div>""")
    
print("seu html foi criado com sucesso!")