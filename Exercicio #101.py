"""
Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetros o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
"""
from datetime import datetime


def voto(idade):
    """
    -> A função voto calcula se a pessoa pode votar ou não
    :param idade: Numero inteiro
    :return: sem retorno
    """
    if 0 < idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO NEGADO')


n = datetime.now().year - int(input('Ano de nascimento: '))
voto(n)
