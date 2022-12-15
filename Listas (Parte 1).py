

num = [2,5,9,1]
num.append(8)           #adiciona um campo a lista e insere o valor na lista, é inserido no final
num.sort()              #organiza em ordem
num.sort(reverse=True)  #organiza invertendo a ordem
num.sort(reverse=False) #inverte a reversao
num.insert(2, 0)        # =append , porem o 1° numero é a cordenada de onde se deseja inserir o 2°
# insero o 0 na posição 2 da lista
num.pop()               #remove o ultimo elemento
num.pop(3)              #remove o elemento na coordenada indicada
num.remove(2)           #remove o n° desejado que estiver no 1° indice encontrado

#logica para remover um numero especifico (ex:999)
if 999 in num:
    num.remove(999)
else:
    print('\nNao foi encontrado o numero 999')
#==============================================

print(f"\n a lista 'num' é :{num}")
print(f"\n essa lista tem {len(num)} elementos")  # len conta o tamanho da lista

#=== PRINTANDO COM FORMATAÇÃO A CADA ELEMENTO ===
import random
valores = []

for c in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
    #i = random.randint(0, 10)      #inserindo valor randomizado
    # valores.append(i)
    print(f" {valores}", end=' ')
print("\n a lista valores é: ",valores)

for b, v in enumerate(valores):
    print(f"Na posição {b} encontrei o valor {v}")
print('cheguei ao final da lista')




























