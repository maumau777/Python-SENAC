# Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar: a. A menor altura do grupo; b. A maior altura do grupo;

alturas = []

for i in range(15):
    while True:
        try:
            altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
            alturas.append(altura)
            break
        except ValueError:
            print("Por favor, insira um número válido para a altura.")

menor_altura = min(alturas)
maior_altura = max(alturas)

print(f"A menor altura do grupo é: {menor_altura} metros")
print(f"A maior altura do grupo é: {maior_altura} metros")
