fat = int(input('Digite um número: '))
'''cont = 1
num = fat
while cont < num:
    fat = fat * cont
    cont += 1
    print('x' if cont > 1 else '=', end='')
print(f'O fatorial deu {fat}')'''
'''from math import factorial
print('O fatorial é', factorial(fat))'''
f = 1
for c in range(1, fat+1):
    f *= c
print(f)
