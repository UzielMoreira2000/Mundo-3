
"""
Exercício Python 079: Crie um programa onde o usuário possa digitar
vários valores numéricos e cadastre-os em uma lista. Caso o número
já exista lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente.
"""

color = {'Vermelho':'\033[1;31m',
         'Amarelo' :'\033[1;33m',
         'Verde'   :'\033[1;32m'}

clean = {'0': '\033[0;0m'}

num = list()

while True:

    n = int(input('\nDigite um valor: '))
    if n not in num : # verifica existencia do n adiciona na lista
        num.append(n)
        print('{}Valor {} adicionado com sucesso...{}'.format(color['Verde'],n,clean['0']))
    else:
        print('{}Valor duplicado! O valor não foi adicionado{}'.format(color['Amarelo'],clean['0']))

    # condição e validação da condição
    r = str(input('Deseja continuar? [S/N]: ')).upper()
    while r not in 'NSns' :
        print('\n{}Opção não reconhecida, por favor selecione uma das opções abaixo.{}'
              .format(color['Vermelho'],clean['0']))
        r = str(input('Deseja continuar? [S/N]: ')).upper()

    if r == 'N':
        break

print('='*35)
num.sort()
print('Voce digitou os valores: {}{}{}'.format(color['Verde'], num,clean['0'] ))
print('\n{}Programa Encerrado com sucesso !'.format(color['Verde']))






















