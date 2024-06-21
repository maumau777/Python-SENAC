import random

nomes = []

while True:
    nome = input("Digite seu nome (Digite -1 para parar): ")

    if nome ==  "-1":
        break
    else:
        nomes.append(nome)

num_pessoas  = len(nomes)
print(f"O número de pessoas é: {num_pessoas}")

ordem_nomes = sorted(nomes)
print("Lista de nomes em ordem alfabética: ")
for nome in ordem_nomes:
    print(nome)

if num_pessoas >= 3:
    print(f"O terceiro da lista é: {ordem_nomes[2]}")
else:
    print("Não há terceiro na lista.")

if num_pessoas > 0:
    ganhador = random.choice(nomes)
    print(f"O nome do ganhador é: {ganhador}")
else:
    print("Nenhum nome foi inserido")
