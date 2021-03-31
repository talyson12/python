valor_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
while True:
    n = int(input('Digite um número entre 0 e 5: '))
    while True:
        if 0 <= n <= 5:
            break
        n = int(input('Valor inválido, digite um número entre 0 e 5: '))
    print('O valor por extenso é:', valor_extenso[n])

    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar (S/N)? '))
    if resp == 'n':
        break
