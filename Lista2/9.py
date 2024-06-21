# Escreva um algoritmo que: • leia um número indeterminado de linhas contendo, cada uma, a idade de um indivíduo. A última linha, que não entrará nos cálculos, contém o valor da idade igual a zero; • calcule e escreva a idade média deste grupo de indivíduos.

soma_idades = 0
contador_individuos = 0

while True:
    try:
        idade = int(input("Digite a idade do indivíduo (ou 0 para terminar): "))
        
        if idade == 0:
            break
        
        soma_idades += idade
        contador_individuos += 1
        
    except ValueError:
        print("Por favor, insira um número válido para a idade.")

if contador_individuos > 0:
    idade_media = soma_idades / contador_individuos
    print(f"A idade média do grupo de indivíduos é: {idade_media:.2f} anos")
else:
    print("Nenhuma idade válida foi inserida.")
