"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média
"""

pessoas = dict()
grupo = list()
total = 0

while True:
    pessoas['nome'] = str(input('Nome: '))

    while True:
        pessoas['sexo'] = str(input('Sexo:[M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F')

    pessoas['idade'] = n = int(input('Idade: '))

    total += n
    grupo.append(pessoas.copy())

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-=' * 30)
        if opcao in 'SN':
            break
        else:
            print('Erro! Responda apenas S ou N')
    if opcao == 'N':
        break

print(f'O grupo tem {len(grupo)} pessoas')
print(f'A média de idade é de {total / len(grupo)}')
print(f'As mulheres cadastradas foram: ', end='')

for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()

print('Lista das pessoas que estão acima da média: ', end='')

for p in grupo:
    if p['idade'] >= total / len(grupo):
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
