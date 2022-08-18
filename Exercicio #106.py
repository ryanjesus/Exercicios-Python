"""
Faça um minisistema que utilize o Interactive Help do Python. O usuário vai
digita o comando e o manual vai aparecer.

Quando o usuário digitar a falavar 'FIM' o program se encerrará

OBS: use cores.
"""

while True:
    res = str(input('Função ou Biblioteca: '))
    if res != 'fim':
        print('-'*30)
        print(f"Acessando o manual do comando '{res}'")
        help(res)
    else:
        break



