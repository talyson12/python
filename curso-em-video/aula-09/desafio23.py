num = int(input('Digite um número entre 0 e 9999: '))
'''print('Unidade:', num[3], '\nDezena:', num[2], '\nCentena:', num[1], '\nMilhar:', num[0])'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade:', u)
print('Dezena:', d)
print('Centena:', c)
print('Milhar:', m)

