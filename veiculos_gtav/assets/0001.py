palavra = ''' <div class="veiculos-container">
  <img src="./images/barcos/img1.png" alt="Vehicle Name">
                    <h2>Kraken</h2>
                    <h3>Barco</h3>
                    <div class="vehicle-stats">'''
                

p2 = " oi oi oi"
contador = 0


lens = len(palavra)


while (contador<lens):
    contador+=1
    print(palavra[contador])
    


# for i,letra in enumerate(palavra):
#     # print(letra)
#     if i > lens-5:
#         break
#     ppp = letra + palavra[i+1] + palavra[i+2] + palavra[i+3]
#     # print(ppp)
#     if ppp=='imag':
#         print(ppp)

# while '<div class="vehicle">' in palavra:
#     contador += 1
#     palavra = palavra.replace('<div class="vehicle">', 'AAAAAAAAAAAAAAAAAAAAA')
#     print(contador)

# print(palavra)