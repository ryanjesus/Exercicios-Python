"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: inicio, fim e passo e realize a contagem.

Seu program tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
a) De 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep
qtd = 0


def contagem(a, b, c):
    if qtd == 1:
        for cont in reversed(range(a, b, c)):
            print(cont, end=' ')
            sleep(0.5)
        print()
    else:
        for cont in range(a, b, c):
            print(cont, end=' ')
            sleep(0.5)
        print()


contagem(1, 11, 1)
qtd += 1

contagem(0, 11, 2)
qtd += 1

print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
if a > b and c > 0:
    qtd = 1
    contagem(b, a, c)
if c == 0:
    contagem(a, b, 1)



