"""
Dentro do pacote utilizadesCev que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários
"""

from utilidadecev import moeda
from utilidadecev import dado


preco = dado.leiaDinehiro('Digite o preço: R$')
moeda.resumo(preco)