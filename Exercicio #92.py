"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário
receberá também o ano de contratação e o salário, Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar
"""

from datetime import datetime
registro = dict()

registro['nome'] = str(input('Nome: '))
registro['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
registro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if registro['ctps'] != 0:
    registro['contratação'] = int(input('Ano de contratação: '))
    registro['salário'] = float(input('Salário: '))
    registro['aposentadoria'] = n = registro['idade'] + ((registro['contratação'] + 35) - datetime.now().year)
print('-='*30)

for v, k in registro.items():
    print(f'{v} tem o valor {k}')
