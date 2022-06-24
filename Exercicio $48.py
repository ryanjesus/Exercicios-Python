""" Faça um programa que calcule a soma entre todos os
número impares que são múltiplos de tês e que se
ecnontram no intervalo de 1 até 500"""
s = 0
for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print(f'A soma de todos os número impares que são multiplos de 3 é: {s}')