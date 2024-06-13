altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ")

def calcular_peso_ideal(altura, sexo):
    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo não reconhecido.")
        return None
    return peso_ideal

peso_ideal = calcular_peso_ideal(altura, sexo)
if peso_ideal is not None:
    print("Seu peso ideal é:", peso_ideal, "quilos.")

# calculo do imc (m/h²)

peso = float(input("Digite seu peso (em quilos): "))

imc = peso/(altura ** 2)
print("Seu IMC é:", imc,".")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade grau 1")
elif 35 <= imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")