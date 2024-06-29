"""
Um armazém trabalha com 10 mercadorias diferentes identificadas pelos
números inteiros de 0 a 9.
O dono do armazém anota a quantidade de cada mercadoria vendida durante o mês.
Ele tem uma tabela que indica para cada mercadoria o preço de venda. Escreva um
algoritmo que leia a quantidade vendida de cada produto no final do mês
(armazenando-os em uma lista Q) e o preço de venda de cada um (armazenando-os
em uma lista P). Logo após calcular e escrever o faturamento mensal do armazém.
"""

Q = []
P = []

for i in range(10):
    q = int(input(f"Digite a quantidade vendida do produto {i}: "))
    Q.append(q)
    p = float(input(f"Digite o preço de venda do produto {i}: "))
    P.append(p)
    print()

faturamento = 0

for i in range(10):
    faturamento += Q[i] * P[i]
    print(f"O faturamento do produto {i} foi de R$ {Q[i] * P[i]}")
    print()

print(f"O faturamento total do mês foi de R$ {faturamento}")