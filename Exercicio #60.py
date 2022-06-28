"""
Faça um programa que leia um número qualquer e mostre o seu fatorial
"""


n = int(input('Digite um numero para calular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
