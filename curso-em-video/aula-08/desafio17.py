import math
catetoOp = float(input('Digite o cateto oposto: '))
catetoAdj = float(input('Digite o cateto adjacente: '))
'''print('O valor da hipotenusa é: {:.2f}'.format(math.sqrt(math.pow(catetoOp, 2) + math.pow(catetoAdj, 2))))'''

print('A hipotenusa é: {:.2f}'.format(math.hypot(catetoOp, catetoAdj)))
