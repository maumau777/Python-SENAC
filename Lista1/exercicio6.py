number = int(input("Digite um número: "))

if number % 3 == 0 and number % 7 == 0:
    print(f"{number} é divisível por 3 e por 7.")
else:
    print(f"{number} não é divisível por 3 e por 7.")