# Crie uma função que receba um número como parâmetro e escreva a tabuada desse número.

def tabuada(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

tabuada(int(input("Digite um número: ")))