"""
Exercício Python 081: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
condicional = ' '
lista.append(int(input('Digite um valor: ')))

while True:

    condicional = str(input('Digite [s/n] para inserir novos valores: ')).upper()

    if condicional == 'S':
        lista.append(int(input('Digite outro valor: ')))
    if condicional == 'N':
        break

lista.sort(reverse=True)

if 5 in lista:

    print(f'\n O valor 5 está na lista', end='')

    #pos = lista.index(5)
    #print(f', na posição: {pos}° ')

else:
    print('\n Nao foi encontrado o numero 5')

print('='*35)
print(f"\n essa lista tem {len(lista)} elementos: {lista}")


