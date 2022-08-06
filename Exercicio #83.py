"""
Crie um programa onde o usuário digite um expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão paddas está com
os parênteses abertos e fechados na ordem correta
"""
qtd = 0
expressao = str(input('Digite a expressão: '))
expressao = list(expressao)
for i in expressao:
    if i in '()':
        qtd += 1

if qtd % 2 == 0:
    print('Sua expressão está correta')
else:
    print('Está faltando coloca um parênteses')