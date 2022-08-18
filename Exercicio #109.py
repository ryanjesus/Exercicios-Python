"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetros a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
desenvolvida no desafio 108
"""

import mod107

preco = float(input('Digite o preço: R$'))
print(f'A metade de {mod107.moeda(preco)} é {mod107.metade(preco, False)}')
print(f'O dobro de {mod107.moeda(preco)} é {mod107.dobro(preco, False)}')
print(f'Aumentando 10%, temos {mod107.aumentar(preco, False)}')
print(f'Reduzindo 13%, temos {mod107.reduzir(preco, False)}')