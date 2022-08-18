"""
Crie um pacote chamdo utilidadesCeV que tenha dois módulos
internos chamados moeda e dado.

Transfira todos as funções utilizada nos desafios 107, 108, 109 para os primeira pacote e mantenha tudo funcionando
"""

from utilidadecev import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco)