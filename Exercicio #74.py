"""
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla

Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla
"""

from random import sample

n = tuple(sample(range(10), 5))
print(n)
print(f'O maior valor é {max(n)} e o menor é {min(n)}')