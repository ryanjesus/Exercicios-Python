"""
Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado

No final, mostre a matriz na tela, com a formatação correta
"""

matriz = [[], [], []]
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {l}]: ')))

for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()