# Tem-se um conjunto de dados contendo a altura e o sexo (M ou F) de 15 pessoas. Faça um algoritmo que calcule e escreva: • a maior e a menor altura do grupo; • a média de altura das mulheres; • número de homens.

alturas = []
sexos = []

soma_alturas_mulheres = 0
contador_mulheres = 0
contador_homens = 0

for i in range(15):
    while True:
        try:
            altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
            sexo = input(f"Digite o sexo da pessoa {i + 1} (M/F): ").strip().upper()
            
            if sexo not in ['M', 'F']:
                print("Por favor, insira 'M' para masculino ou 'F' para feminino.")
                continue
            
            alturas.append(altura)
            sexos.append(sexo)
            
            if sexo == 'F':
                soma_alturas_mulheres += altura
                contador_mulheres += 1
            elif sexo == 'M':
                contador_homens += 1

            break
        except ValueError:
            print("Por favor, insira um número válido para a altura.")

maior_altura = max(alturas)
menor_altura = min(alturas)

if contador_mulheres > 0:
    media_altura_mulheres = soma_alturas_mulheres / contador_mulheres
else:
    media_altura_mulheres = 0

print(f"A maior altura do grupo é: {maior_altura:.2f} metros")
print(f"A menor altura do grupo é: {menor_altura:.2f} metros")
print(f"A média de altura das mulheres é: {media_altura_mulheres:.2f} metros")
print(f"O número de homens no grupo é: {contador_homens}")
