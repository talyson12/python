from time import sleep
priTermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
nTermos = 1
c = 0
while nTermos <= 10:
    print(priTermo + razão * c,end='')
    print(', ' if nTermos < 10 else '', end='')
    nTermos += 1
    c += 1
    sleep(0.5)
