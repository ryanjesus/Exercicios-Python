"""
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vercer
"""

import random

numero_digitado = 0
tentativa = 0

lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteio = random.choice(lista_numero)
while numero_digitado != sorteio:
    numero_digitado = int(input('Digite um número: '))
    tentativa += 1
    if numero_digitado != sorteio:
        print('Numero errado')
    else:
        print('Você acertou!')
print(f'Você precisou de {tentativa} tentativas para acerta')
