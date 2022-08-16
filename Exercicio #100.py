"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai coloca-los dentros da lista e a segunda função vai
mostrar a soma entre todos os valores PARES sorteados pela função anterior
"""

numeros = list()
from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n} ', end='')
    print()



def somarPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
somarPar(numeros)