import random

marido=["João","José","Lucas"]
esposa=["Maria","Lucia","Amanda"]

random.seed()
x = random.randint(0,4)
n=int(input('Escolha seu sexo 1-Homem e 2-Mulher e pressione [ENTER]:'))
print("Número Sorteado:",x)
if n==1:
    print('Você vai casar com a',esposa[x])
elif n==2:
    print('Você vai casar com o',marido[x])
else:
    print('Você não vai casar')

