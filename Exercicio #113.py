"""
Reecreva a função leiaInt() que fizemos no desafio 104. incluindo agora a possivilidade da digitação
de um número de tipo inválido.

Aproveite e crie também uma função LeiaFloot() com a mesma funcionalidade
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


try:
    n = leiaInt('Digite um número: ')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar esse numero')
    n = 0
    print(f'Não foi digitado valor por isso é {n}')
else:
    print(f'Você acabou de digitar o número {n}')