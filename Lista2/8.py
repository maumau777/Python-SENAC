# Escreva um algoritmo que receba a idade de 10 pessoas, calcule e imprima a quantidade de pessoas maiores de idade (idade >= 18 anos).

idades = []

for i in range(10):
    while True:
        try:
            idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
            idades.append(idade)
            break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

maiores_de_idade = 0

for idade in idades:
    if idade >= 18:
        maiores_de_idade += 1

print(f"A quantidade de pessoas maiores de idade é: {maiores_de_idade}")
