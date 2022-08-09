"""
Crie um programa onde 4 jogadores tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dados
"""

from random import randint
import time

jogadores = dict()
n = 0

for j in range(1, 5):
    jogadores[f'jogandor{j}'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    time.sleep(0.5)
print('-'*30)
print('Ranking dos jogandores')

for k in sorted(jogadores, key=jogadores.get, reverse=True):
    time.sleep(0.5)
    n += 1
    print(f'{n}ª Lugar: {k} com {jogadores[k]}')
