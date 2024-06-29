# Crie uma função para receber o ano corrente e o ano de nascimento de uma pessoa. Em seguida, retorne à idade da pessoa.

def idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

print(idade(ano_atual, ano_nascimento))
