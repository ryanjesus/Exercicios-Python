"""Desenvolva um program que leia o primeiro termo e a razão de uma PA.
no final, mostre os 10 primeiros termos dessa progessão"""

termo = int(input("Digite o primeir termo: "))
razao = int(input("Digite a razão: "))

for c in range(termo, 10, razao):
    print(c)
