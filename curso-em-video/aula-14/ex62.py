from time import sleep
priTermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
nTermos = 1
while nTermos <= 10:
    print(priTermo + razão * (nTermos - 1), end=', ')
    nTermos += 1
    sleep(0.5)
op = str(input('Deseja continuar? (S/N)')).strip().lower()
termoGeral = priTermo + razão * 10
if op == 's':
    while op == 's':
        nTermos = int(input('Desejas mostrar quantos termos? '))
        c = 1
        while c <= nTermos:
            print(termoGeral + razão * (c - 1), end=', ')
            sleep(0.5)
            c += 1
        op = str(input('Quer continuar? (S/N)'))
        termoGeral = termoGeral + razão * nTermos
else:
    print('FIM')
