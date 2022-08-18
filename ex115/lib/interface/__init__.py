"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples

O sistema só vai ter 2 opções: cadastrar um nova pessoa e listar todas as pessoas cadastradas
"""


def leiaInt(txt='0'):
    ok = False
    valor = 0

    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número inteiro válido')

        if ok:
            break
    return valor


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
