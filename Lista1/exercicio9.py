sigla_estado = input("Digite a sigla do estado (RJ, SP, MG, etc.): ")
sigla_estado = sigla_estado.upper()

if sigla_estado == "RJ":
    print("Legal! Você é cario-- OLHA O TIRO, CUIDADO!!!")
elif sigla_estado == "SP":
    print("Que pena! Você é paulista :(")
elif sigla_estado == "MG":
    print("Uai, então ocê é mineiro zé?.")
else:
    print("Legal! Você é de outro estado.")