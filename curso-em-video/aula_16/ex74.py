from random import randint
tupla = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print(tupla)
# print('Menor', min(tupla))
# print('Maior', max(tupla))
print('Menor', sorted(tupla)[0])
print('Maior', sorted(tupla)[4])
