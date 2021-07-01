lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche[-4:]) # Pudim pode ser o lanche[3] ou lanche[-1], os atrás dele vão ser lanche[2]e assim por diante
'''for comida in lanche: # para cada comida que que se encontra dendo da variável composta lanche faça
    print(comida, end=' ') # imprima'''
'''for cont in range(0, len(lanche)):
    print(lanche[cont], end=' ')'''
for posição, comida in enumerate(lanche):
    print(f'Posição {posição} comida {comida}')
print(sorted(lanche))
a = (2, 1)
b = (3, 4, 2)
c = a + b
print(c)
print(c.count(1)) # quantas vezes o número 1 aparece
print(c.index(4)) # em que posição está o 4
# print(c.index(2, 3)) # quantos 2 tem a partir da posição 1
del(lanche) # apaga a tupla inteira, não é possível deletar um elemento da tupla
