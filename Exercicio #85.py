"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e impares.

No final, mostre os valores pares e impares em ordem crescente
"""

num = [[], []]
n = 0

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Lista de numero pares {num[0].sort()}')
print(f'Lista de numeros impares {num[1].sort()}')

