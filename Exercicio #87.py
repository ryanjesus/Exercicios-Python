"""
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados
B) A soma dos valore da terceira coluna
c) O maior valor da segunda linha
"""

matriz = [[], [], []]
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {l}]: ')))

for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()