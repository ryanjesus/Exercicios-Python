"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade()

Faça também um programa que importe esse módulo e use algumas dessas funções
"""
import mod107


preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {mod107.metade(preco)}')
print(f'O dobro de {preco} é {mod107.dobro(preco)}')
print(f'Aumentando 10%, temos {mod107.aumentar(preco)}')
print(f'Reduzindo 13%, temos {mod107.reduzir(preco)}')