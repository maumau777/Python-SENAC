'''
Crie uma função que receba por parâmetro um número inteiro e verifique
quantas vezes esse valor se encontra em uma lista (declarada globalmente). Retorne
a quantidade de vezes que o valor se encontra na lista.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def verifica(num):
    global lista
    cont = 0
    for n in lista:
        if n == num:
            cont += 1
    return cont

num = int(input("Digite um número: "))

print(f"O número {num} aparece {verifica(num)} vezes na lista.")