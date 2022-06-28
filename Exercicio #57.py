"""
Faça um programa que leia o sexo de uma pesssoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peçaa digitação novamente até ter um valor corretor
"""

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o seu sexo [F/M] ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Apenas [F/M]')
print('Fim')