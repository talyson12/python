lista = [0, 1, 2, 3, 4, 5]
lista.append(6) # adicionei o valor 6 na última posição
lista.insert(0, 7) # adicionei na posição 0 o valor 7
print(lista)
tupla =(1, 3, 4)
# del tupla apaga a tupla inteira
del lista[0] # apaga o elemento na posição 0
# ou lista.pop() ou lanche.pop() que elimina o último elemento lanche.remove() <-- nesse caso você indica o valor não o parâmetro
print(tupla, lista)
lista = list(range(4, 11))
print(lista)
# lista.sort() põe a LISTA em ordem ou lista.sort(reverse=True)
# tupla.sorted() põe a TUPLA em ordem
tupla = sorted(tupla)
print(tupla)

valores = []
valores.append(1)
valores.append(5)
valores.append(6)
valores.append(3)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
if 3 in valores:
    valores.pop(3)
else:
    print('Encontrei nada')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)