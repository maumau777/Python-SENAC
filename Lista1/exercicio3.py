import math

number = float(input("Digite algum número: "))

if number >= 0:
    raiz_quadrada = math.sqrt(number)
    print(f"A raiz quadrada de {number} é {raiz_quadrada}.")
else:
    quadrado = number ** 2
    print(f"O quadrado de {number} é {quadrado}.")