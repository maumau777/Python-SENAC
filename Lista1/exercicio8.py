ano_nasc = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

if ano_nasc > 0:
    idade = ano_atual - ano_nasc
    print(f"A sua idade atual é: {idade}")
else:
    print(f"O ano de seu nascimento informado ({ano_nasc}) é inválido!")