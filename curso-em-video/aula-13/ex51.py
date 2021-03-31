a1 = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
for c in range(1, 11):
    print(f'a{c} = {a1}', end=' | ')
    a1 += razão
