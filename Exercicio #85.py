"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e impares.

No final, mostre os valores pares e impares em ordem crescente
"""

par = list()
impar = list()

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Lista de numero pares {sorted(par)}')
print(f'Lista de numeros impares {sorted(impar)}')