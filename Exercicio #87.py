"""
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados
B) A soma dos valore da terceira coluna
c) O maior valor da segunda linha
"""

matriz = [[], [], []]
par = col3 = 0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {l}]: ')))
        par += matriz[c][l] if matriz[c][l] % 2 == 0 else 0
        col3 += matriz[c][l] if l == 2 else 0
print('-' * 35, *matriz, sep='\n')  # Mostra a matriz
print('-' * 35, f'\nA soma dos números pares é {par}')
print(f'A soma dos números da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')