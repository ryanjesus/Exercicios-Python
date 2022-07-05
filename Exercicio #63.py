"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma Sequência de Fibonacci
"""
n = int(input('A sequência de Fibonacci de: '))
a, b = 0, 1
while a < n:
    print(a, end=', ')
    a, b = b, a+b
print('FIM')