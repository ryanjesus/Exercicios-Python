"""
Adapte o codigo do desafio 107, criando uma função adicional chamada moeda() que consiga mostras
os valores como um valor monetário formatado
"""

import mod107

preco = float(input('Digite o preço: R$'))
print(f'A metade de {mod107.moeda(preco)} é {mod107.moeda(mod107.metade(preco))}')
print(f'O dobro de {mod107.moeda(preco)} é {mod107.moeda(mod107.dobro(preco))}')
print(f'Aumentando 10%, temos {mod107.moeda(mod107.aumentar(preco))}')
print(f'Reduzindo 13%, temos {mod107.moeda(mod107.reduzir(preco))}')