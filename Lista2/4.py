# Algoritmo para contar votos de uma eleição com três candidatos

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_brancos = 0
votos_nulos = 0
total_eleitores = 0

print("Digite o voto de cada eleitor. (1, 2, 3 para candidatos, 0 para branco, 4 para nulo, -1 para finalizar):")

while True:
    voto = int(input("Digite o voto: "))
    
    if voto == -1:
        break 
    
    total_eleitores += 1  
    
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 0:
        votos_brancos += 1
    elif voto == 4:
        votos_nulos += 1
    else:
        print("Voto inválido. Tente novamente.")

if votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3:
    vencedor = "Candidato 1"
elif votos_candidato2 > votos_candidato1 and votos_candidato2 > votos_candidato3:
    vencedor = "Candidato 2"
elif votos_candidato3 > votos_candidato1 and votos_candidato3 > votos_candidato2:
    vencedor = "Candidato 3"

print("\nResultados da eleição:")
print(f"Total de eleitores: {total_eleitores}")
print(f"Votos em branco: {votos_brancos}")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos para o Candidato 1: {votos_candidato1}")
print(f"Votos para o Candidato 2: {votos_candidato2}")
print(f"Votos para o Candidato 3: {votos_candidato3}")
print(f"Candidato vencedor: {vencedor}")
