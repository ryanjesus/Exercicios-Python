"""
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
brasil.append(pessoa)
"""


"""
Faça um programa que leia nome e média de um aluno, gaurdando também a situação em
um dicionário. No final, mostre o conteúdo da estrutura na tela
"""

aluno = dict()

aluno['nome'] = str(input('Digite no nome do aluno: '))
aluno['média'] = float(input(f'Digite a média {aluno["nome"]}: '))

print(f'O aluno(a) {aluno["nome"]} teve a média acima de 6 então passou') if aluno["média"] >= 6 else print(f'O aluno(a) {aluno["nome"]} teve a média abaixo de 6 então não passou')