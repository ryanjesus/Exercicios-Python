"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor pesos lidos"""


lista = []
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c} pessoa: '))
    lista += [peso]
print(f'O maior peso foi {max(lista)}')
print(f'O menor peso foi {min(lista)}')

