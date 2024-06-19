idade = int(input("Digite sua idade: "))

if idade < 16:
    print("NÃO ELEITOR!")
elif 18 <= idade < 65:
    print("ELEITOR OBRIGATÓRIO!")
else:
    print("ELEITOR FACULTATIVO!")