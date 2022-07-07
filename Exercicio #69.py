"""
Crie um programa que leia a idade e o sexo de várias peassos. A cada pessoa
cadastrada, o programa deverá pergunta se o usuário quer ou não continuar.

No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos
"""


contidade = contisexom = contisexof = 0


while True:
    print('-=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-=-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        contidade += 1
    if sexo == 'F' and idade < 20:
        contisexof += 1
    if sexo == 'M':
        contisexom += 1
    if q == 'N':
        print('Saindo do programa! ')
        break
print('-=-' * 20)
print(f'{contidade} são maiores de 18 anos')
print('-=-' * 20)
print(f'{contisexom} são homens')
print('-=-' * 20)
print(f'{contisexof} mulheres são menor de 20 anos')