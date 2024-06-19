import math

a = float(input("Digite algum número: "))
b = float(input("Digite algum número: "))
c = float(input("Digite algum número: "))

if a == 0:
    print("Impossível realizar. O coeficiente a deve ser diferente de zero. Não é uma equação do segundo grau.")
else:
    delta = b**2 - 4 * a * c
    if delta >= 0:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")
    else:
        print("Não há raízes reais. Delta é negativo.")
