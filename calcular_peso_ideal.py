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
