listagem = ('lápis', 1.75,
            'borracha', 2.00,
            'caderno', 15.90,
            'estojo', 19.60,
            'mochila', 29.78)
for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}', end='')
    else:
        print(f'R${listagem[posição]:>7.2f}')
