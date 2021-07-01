import math
#from math import sqrt, ceil, floor
#from math import sqrt as raizquadrada - agora ao invés de math.sqrt, pode simplismente usar math.raizquadrada
num = int(input('Digite um número: '))
print('A raíz de {} é: {:.2f}\nPra cima é {}\nPra baixo é: {}'.format(num, math.sqrt(num), math.ceil(math.sqrt(num)), math.floor(math.sqrt(num))))

import random
#num = random.random() #número float entre 0 e 1
num = random.randint(1, 10)
print('Número aleatório:', num)
