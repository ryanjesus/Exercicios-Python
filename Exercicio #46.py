"""Faça um programa que mostre na tela um contagem
regressiva para o estouro de fogos de artifcio, indo de 10
até 0, com uma de 1 sengundo entre eles"""

import time
print('-=-'*20)
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('Feliz Ano Novo')
