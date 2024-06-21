# Escreva um algoritmo que receba números do usuário enquanto eles forem positivos e ao fim o algoritmo deve imprimir quantos números foram digitados.

lista = 0

while True:
    numero = int(input("Digite um número: "))
    if numero > 0:
        lista += 1
    else:
        break

print(f"Você digitou {lista} números positivos.")