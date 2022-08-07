"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear números
entre 1 e 60 para cadas jogo, cadastrando tudo em uma lista composta.
"""

from random import randint

lista = list()
qtd = 0

jogos = int(input('Quantos jogos quer criar? '))
for n in range(0, jogos):
    # for l in range(0, 1):
    while qtd < 6:
        sorte = randint(1, 60)
        if sorte not in lista:
            lista.append(sorte)
            qtd += 1
    qtd = 0
    print(f'Jogo numero {n} {sorted(lista)}')
    lista.clear()
