def pular_linha():
    print('\n')

lista_brasileirão = ('Flamengo', 'Vasco', 'Corinthians', 'Fluminense', 'São Paulo', 'Chapecoense')

# print(f'Lista de times {lista_brasileirão}', end='\n\n')
cont = 0
for time in lista_brasileirão:
    cont += 1
    print(time, end='')
pular_linha()
print('5 primeiros colocados:', lista_brasileirão[0:5])
print('Os últimos 4 colocados:', lista_brasileirão[-4:])
print('Em ordem alfabética', sorted(lista_brasileirão))
print(f"{lista_brasileirão.index('Chapecoense')}ª posição") # em qual posição está o elemento Chapecoense
