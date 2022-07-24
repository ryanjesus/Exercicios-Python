"""
Desenvolva um program que leia quatro valores pelo o teclado e guarde-os
em uma tuplas. No final, mostre:

A) Qauntas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
"""
v = tuple(int(input('Digite os valores'))for c in range(1, 5))
print(f'O numero nove aparece {v.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {v.index(3)+1}º posição' if 3 in v else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in v if n % 2 == 0}, end=' ')

