"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de uma jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostra a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente
"""


def ficha(nome='<desconhecido>', gols=0):

    print('-'*20)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


n1 = str(input('Nome do jogador: '))
n2 = str(input('Números de Gols: '))

if n2.isnumeric():
    n2 = int(n2)
else:
    n2 = 0

if n1.strip() == '':
    ficha(gols=n2)
else:
    ficha(n1, n2)


