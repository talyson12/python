from time import sleep
'''for c in range(0, 11): #para c de 0 até 11 (para no 11, só mostra até o 10, de 1 em 1)
    print(c)
    sleep(0.5)
print('ACABOU')'''

'''c = int(0)
while c <= 10:
    print(c)
    sleep(0.5)
    c += 1
print('ACABOU')'''

cont = int(input('Você quer contar até onde? '))
c = int(1)
while c <= cont:
    print(c, end=' ')
    sleep(0.2)
    c += 1
print('ACABOU')
