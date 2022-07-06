"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo
"""
n = 0
contador = 1
n = int(input('Quer ver a tabuada de qual valor? '))

while contador < 10:
    if n < 0:
        break
    else:
        print(f'{n} x {contador} = {n * contador}')
        contador += 1
        if contador == 10:
            contador = 0
            n = int(input('Quer ver a tabuada de qual valor? '))
print('PROGRAMA TABUA ENCERRADO.')