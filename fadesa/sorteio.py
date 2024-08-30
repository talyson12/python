from random import choice as escolhido
from random import shuffle as embaralhar

nomes = []

quantidade = int(input('Quantos nomes você vai querer? '))
 
for i in range(quantidade):
    nome = input(f'Digite o {i + 1}º nome: ')
    nomes.append(nome)

'''print('Os nomes digitados foram:')
for i in range(len(nomes)):
    print('{:=^20}'.format(nomes[i]))'''    
embaralhar(nomes)
print(f'A ordem de apresentação será {nomes}')
# print(f'\n\nO nome escolhido foi: {escolhido(nomes)}')