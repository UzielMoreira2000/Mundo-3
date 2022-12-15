"""
Exercício Python 080: Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista
ordenada na tela.
"""

lista = []

for c in range (0, 5):
    n = (input('\nDigite um valor: '))
    # caso seja o primeiro ou
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            # se o inserido for menor que o indice ele é inserido na menor posição
            if n <= lista[pos]:
                #insere na posição atual o valor de n
                lista.insert(pos, n)
                break
            pos += 1
            print(pos)
    print(lista)

print('='*35)
print(f"\nOs valores que voce digitou, assumem a siguinte sequencia: {lista}")

