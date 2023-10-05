#Jogo da velha

#Escolhendo X ou O
while True:
    jogador1 = input("Jogador 1, escolha X ou O: ") .upper()

    if jogador1 == 'X' or jogador1 == 'O':
        if jogador1 == 'X':
            jogador2 = 'O'

        elif jogador1 == 'O':
            jogador2 = 'X'

        print(f"\nJogador 1 escolheu {jogador1}")
        print(f"Jogador 2 será {jogador2}")

        break

    else:
        print("\nSÍMBOLO INVÁLIDO. Por favor escolha X ou O")

#Formação do tabuleiro
matriz = []
ordem = 3

for i in range(ordem):
    elemento = []
    for j in range(ordem):
        elemento.append('_')
    matriz.append(elemento)

print()
print("Este é o tabuleiro: \n")
for i in range(ordem):
    print(matriz[i])

#Rodada 1
while True:
    r1j1 = input("\nJogador 1, digite o número da linha e da coluna: ")
    linhaj1, colunaj1 = r1j1.split()
    linhaj1 = int(linhaj1)
    colunaj1 = int(colunaj1)

    print()
    matriz[linhaj1 - 1][colunaj1 - 1] = jogador1

    for i in range(ordem):
        print(matriz[i])

    r1j2 = input("\nJogador 2, digite o número da linha e da coluna: ")
    linhaj2, colunaj2 = r1j2.split()
    linhaj2 = int(linhaj2)
    colunaj2 = int(colunaj2)

    print()
    matriz[linhaj2 - 1][colunaj2 - 1] = jogador2

    for i in range(ordem):
        print(matriz[i])

    break

#Rodada 2
while True:
    r2j1 = input("\nJogador 1, digite o número da linha e da coluna: ")
    linhaj1, colunaj1 = r2j1.split()
    linhaj1 = int(linhaj1)
    colunaj1 = int(colunaj1)

    print()
    matriz[linhaj1 - 1][colunaj1 - 1] = jogador1

    for i in range(ordem):
        print(matriz[i])

    r2j2 = input("\nJogador 2, digite o número da linha e da coluna: ")
    linhaj2, colunaj2 = r2j2.split()
    linhaj2 = int(linhaj2)
    colunaj2 = int(colunaj2)

    print()
    matriz[linhaj2 - 1][colunaj2 - 1] = jogador2

    for i in range(ordem):
        print(matriz[i])

    break

#Rodada 3
while True:
    r3j1 = input("\nJogador 1, digite o número da linha e da coluna: ")
    linhaj1, colunaj1 = r3j1.split()
    linhaj1 = int(linhaj1)
    colunaj1 = int(colunaj1)

    print()
    matriz[linhaj1 - 1][colunaj1 - 1] = jogador1

    for i in range(ordem):
        print(matriz[i])

    if jogador1 == matriz[0][0] == matriz[1][1] == matriz[2][2] or jogador1 == matriz[0][2] == matriz[1][1] == matriz[2][0]:
        print("\nJogador 1 venceu")
        break
    elif jogador1 == matriz[0][0] == matriz[0][1] == matriz[0][2] or jogador1 == matriz[1][0] == matriz[1][1] == matriz[1][2] or jogador1 == matriz[2][0] == matriz[2][1] == matriz[2][2]:
        print("\nJogador 1 venceu")
        break
    elif jogador1 == matriz[0][0] == matriz[1][0] == matriz[2][0] or jogador1 == matriz[0][1] == matriz[1][1] == matriz[2][1] or jogador1 == matriz[0][2] == matriz[1][2] == matriz[2][2]:
        print("\nJogador 1 venceu")
        break

    r3j2 = input("\nJogador 2, digite o número da linha e da coluna: ")
    linhaj2, colunaj2 = r3j2.split()
    linhaj2 = int(linhaj2)
    colunaj2 = int(colunaj2)

    print()
    matriz[linhaj2 - 1][colunaj2 - 1] = jogador2

    for i in range(ordem):
        print(matriz[i])

    if jogador2 == matriz[0][0] == matriz[1][1] == matriz[2][2] or jogador2 == matriz[0][2] == matriz[1][1] == matriz[2][0]:
        print("\nJogador 2 venceu")
        break
    elif jogador2 == matriz[0][0] == matriz[0][1] == matriz[0][2] or jogador2 == matriz[1][0] == matriz[1][1] == matriz[1][2] or jogador2 == matriz[2][0] == matriz[2][1] == matriz[2][2]:
        print("\nJogador 2 venceu")
        break
    elif jogador2 == matriz[0][0] == matriz[1][0] == matriz[2][0] or jogador2 == matriz[0][1] == matriz[1][1] == matriz[2][1] or jogador2 == matriz[0][2] == matriz[1][2] == matriz[2][2]:
        print("\nJogador 2 venceu")
        break

    break

#Rodada 4
while True:
    r4j1 = input("\nJogador 1, digite o número da linha e da coluna: ")
    linhaj1, colunaj1 = r4j1.split()
    linhaj1 = int(linhaj1)
    colunaj1 = int(colunaj1)

    print()
    matriz[linhaj1 - 1][colunaj1 - 1] = jogador1

    for i in range(ordem):
        print(matriz[i])

    if jogador1 == matriz[0][0] == matriz[1][1] == matriz[2][2] or jogador1 == matriz[0][2] == matriz[1][1] == matriz[2][0]:
        print("\nJogador 1 venceu")
        break
    elif jogador1 == matriz[0][0] == matriz[0][1] == matriz[0][2] or jogador1 == matriz[1][0] == matriz[1][1] == matriz[1][2] or jogador1 == matriz[2][0] == matriz[2][1] == matriz[2][2]:
        print("\nJogador 1 venceu")
        break
    elif jogador1 == matriz[0][0] == matriz[1][0] == matriz[2][0] or jogador1 == matriz[0][1] == matriz[1][1] == matriz[2][1] or jogador1 == matriz[0][2] == matriz[1][2] == matriz[2][2]:
        print("\nJogador 1 venceu")
        break

    r4j2 = input("\nJogador 2, digite o número da linha e da coluna: ")
    linhaj2, colunaj2 = r4j2.split()
    linhaj2 = int(linhaj2)
    colunaj2 = int(colunaj2)

    print()
    matriz[linhaj2 - 1][colunaj2 - 1] = jogador2

    for i in range(ordem):
        print(matriz[i])

    if jogador2 == matriz[0][0] == matriz[1][1] == matriz[2][2] or jogador2 == matriz[0][2] == matriz[1][1] == matriz[2][0]:
        print("\nJogador 2 venceu")
        break
    elif jogador2 == matriz[0][0] == matriz[0][1] == matriz[0][2] or jogador2 == matriz[1][0] == matriz[1][1] == matriz[1][2] or jogador2 == matriz[2][0] == matriz[2][1] == matriz[2][2]:
        print("\nJogador 2 venceu")
        break
    elif jogador2 == matriz[0][0] == matriz[1][0] == matriz[2][0] or jogador2 == matriz[0][1] == matriz[1][1] == matriz[2][1] or jogador2 == matriz[0][2] == matriz[1][2] == matriz[2][2]:
        print("\nJogador 2 venceu")
        break

    break

#Rodada 5
while True:
    r5j1 = input("\nJogador 1, digite o número da linha e da coluna: ")
    linhaj1, colunaj1 = r5j1.split()
    linhaj1 = int(linhaj1)
    colunaj1 = int(colunaj1)

    print()
    matriz[linhaj1 - 1][colunaj1 - 1] = jogador1

    for i in range(ordem):
        print(matriz[i])

    if jogador1 == matriz[0][0] == matriz[1][1] == matriz[2][2] or jogador1 == matriz[0][2] == matriz[1][1] == matriz[2][0]:
        print("\nJogador 1 venceu")
        break
    elif jogador1 == matriz[0][0] == matriz[0][1] == matriz[0][2] or jogador1 == matriz[1][0] == matriz[1][1] == matriz[1][2] or jogador1 == matriz[2][0] == matriz[2][1] == matriz[2][2]:
        print("\nJogador 1 venceu")
        break
    elif jogador1 == matriz[0][0] == matriz[1][0] == matriz[2][0] or jogador1 == matriz[0][1] == matriz[1][1] == matriz[2][1] or jogador1 == matriz[0][2] == matriz[1][2] == matriz[2][2]:
        print("\nJogador 1 venceu")
        break
    else:
        print("\nVELHOU")
        break