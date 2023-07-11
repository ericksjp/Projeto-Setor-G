import requests
from bs4 import BeautifulSoup
import os

url = input("Informe a ulr do site -> ")
diretorio = input("Informe onde as Imagens serão guardadas-> ")
classe = input ("Informe qual a classe de veiculos: ")
descricao = input ("Faça uma descrião para essa classe: ")


r = requests.get(url)

# Transforma o conteúdo em um objeto BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

images=[]
for i, td in enumerate(soup.find_all('img')):
    texto = td.get('src')
    images.append(texto)
    
    
if not os.path.exists(f'images/{diretorio}'):
    os.mkdir(f'images/{diretorio}')


c=0
for i in images:
    response = requests.get(i)

    with open(f'images/{diretorio}/img{c}.png', 'wb') as f:
        f.write(response.content)
    c+=1

nome = []

for i, td in enumerate(soup.find_all('h2')):
    texto = td.text.strip()
    if not any(s in texto for s in [
        "Further Adventures in Finance and Felony",
        "DLC", 
        "January update 2016", 
        "Further Adventures in Finance and Felony",
        "Cunning Stunts",
        "Import/Export",
        "Gunrunning",
        "Independence Day Special",
        "Smuggler's Run",
        "The Doomsday Heist",
        "Southern San Andreas Super Sport Series"
        ,"After Hours","Arena Wars",
        "The Diamond Casino & Resort",
        "The Diamond Casino Heist",
        "The Doomsday Heist",
        "Exclusive cars",
        "DLC Heists Update",
        "Smuggler`s Run",
        "San Andreas Flight School Update",
        "Race Cars",
        "Race cars",
        "Further Aventures in Finance and Felony",
        "The Diamon Casino Heist",
     ]):
        nome.append(texto)
        
lista = []
for i, td in enumerate(soup.find_all('span')):
    texto = td.text.strip() # pega apenas o texto do elemento e remove espaços em branco
    if texto.isdigit():
        lista.append(int(texto))

# print(lista)
speed_n = [0]
c=0
for i in range(500):
    c+=4
    speed_n.append(c)

braking_n=[1]
c=1
for b in range(500):
    c+=4
    braking_n.append(c)
    
acceleration_n=[2]
c=2
for d in range(500):
    c+=4
    acceleration_n.append(c)
    
    
handling_n=[3]
c=3
for e in range(500):
    c+=4
    handling_n.append(c)
    
velo = []
frenagem = []
aceleracao = []
tracao = []

a =len(lista)
for t in range(a):
    if t in speed_n:
        velo.append(lista[t])
    if t in braking_n:
        frenagem.append(lista[t])
    if t in acceleration_n:
        aceleracao.append(lista[t])
    if t in handling_n:
        tracao.append(lista[t])
        
# print (len(velo))
# print (len(frenagem))
# print (len(aceleracao))
# print (len(tracao))

nome_arquivo = f'{classe}.txt'

# Verifica se o arquivo já existe
if not os.path.exists(nome_arquivo):
    # Cria o arquivo de texto vazio
    with open(nome_arquivo, 'w') as f:
        pass


with open(f'{classe}.txt', 'a') as f:
    f.write(f"""
            <div class="super">
                <div class="introducao">
                    <h3>{classe}s</h3>
                    <p>{descricao}</p>
                </div>
    """)
a= len(nome)
    
for w in range(a):
    with open(f'{classe}.txt', 'a') as f:
        f.write(f"""
                <div class="vehicle">
                    <img src="./images/{diretorio}/img{w}.png" alt="Vehicle Name">
                    <h2>{nome[w]}</h2>
                    <h3>{classe}</h3>
                    <div class="vehicle-stats">
                        <p>Speed:</p>
                        <div class="bar">
                            <div class="fill" style="width: {velo[w]}%;"></div>
                        </div>
                        <p>Acceleration:</p>
                        <div class="bar">
                            <div class="fill" style="width: {frenagem[w]}%;"></div>
                        </div>
                        <p>Handling:</p>
                        <div class="bar">
                            <div class="fill" style="width: {aceleracao[w]}%;"></div>
                        </div>
                        <p>Braking:</p>
                        <div class="bar">
                            <div class="fill" style="width: {tracao[w]}%;"></div>
                        </div>
                    </div>
                </div>
        """)

with open(f'{classe}.txt', 'a') as f:
    f.write("""
            </div>""")
    
print("seu html foi criado com sucesso!")