from random import randint
from time import sleep
numC = randint(0, 5)
print('-=-' * 20)
sleep(2)
print('hmm, estou a pensar...')
sleep(2)
print('-=-' * 20)
sleep(2)
numP = int(input('Digite um número: '))
print('Você acertou!' if numP == numC else 'Tente novamente!')
print('Número que eu pensei >>', numC)
