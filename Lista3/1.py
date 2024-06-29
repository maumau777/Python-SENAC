# Escreva um algoritmo que leia 10 números, armazenando-os em uma lista e mostre o maior número e em que índice se encontra.

numeros = []
maior = 0
indice = 0

for n in range(1, 11):
    numero = int(input(f"Digite o {n}º número: "))
    numeros.append(numero)
    if maior < numero:
        maior = numero
        indice = n
    print(numeros)
    print(f"O maior número é {maior} e está no índice {indice}.")
    print(f"Lista dos números: {numeros}")
    print(f"Maior número: {maior} | Seu índice é: {indice}")
    print("=" * 30)