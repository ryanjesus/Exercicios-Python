"""
- interactive Help help() or print(input.__doc__)
- docstrings -> Cria documentação de def
- Argumentos opcionais c=0
- Escopo de variáveis
- Retono de resultados
"""

def fatorial(n=1):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num = int(input('Digite um valor?: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')