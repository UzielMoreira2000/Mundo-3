"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.
"""

l = []
c = 0
maior = 0
menor = 0

for c in range (0, 5):

    l.append(int(input(f'Digite um valor para posição {c}° : ')))

    if c == 0:
        maior = l[c]
        menor = l[c]
    else:
        if l[c] > maior:
            maior = l[c]
        if l[c] < menor:
            menor = l[c]

print('='*30)
print(f'Voce digitou os valores: {l}')
# Estrutura para apresentão dos termos maoir e menor da lista l[]
print(f'\nO maior valor foi {maior} nas posiçoões : ',end=' ')
for i,v in enumerate(l): # i é o indice do laço e v é o valor obtido pelo enumerate de l[]
    if v == maior:
        print(f'{i}',end='...')

print(f'\nO menor valor foi {menor} nas posiçoões : ',end=' ')
for i,v in enumerate(l): # i é o indice do laço e v é o valor obtido pelo enumerate de l[]
    if v == menor:
        print(f'{i}',end='...')

print('\n\nCheguei ao final da lista !')
























