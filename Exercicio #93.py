"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de golds
feitos em cadas partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durantes o campeonato.
"""

jogador = dict()
temp = list()

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(0, partidas):
    temp.append(int(input(f'Quantos gols na partida {p + 1}? ')))

jogador['gols'] = temp[:]
jogador['total'] = sum(temp)
temp.clear()

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogando {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for p in range(0, partidas):
    print(f'Na partida {p + 1}, fez {jogador["gols"][p]} gols')