""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""

n = int(input("Digite um número: "))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end= '')
        tot += 1
    else:
        print('\033[m', end= '')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {n} foi divisível {tot} vezes')
if tot == 2:
    print('Por esse motivo é um numero primo')
else:
    print('Por esse motivo não é primo')