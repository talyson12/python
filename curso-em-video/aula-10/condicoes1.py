nome = str(input('Digite o seu primeiro nome: ')).strip().lower()
'''if nome == 'gustavo':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome.title()))'''

n1 = float(input('Digite a sua 1º nota: '))
n2 = float(input('Digite a sua 2º nota: '))
m = (n1 + n2) / 2
'''if m >= 7:
    print('Média boa!')
else:
    print('Sua média foi ruim, じゃあ、今度勉強行きませんか?')
print('Caro {}, sua média foi {:.2f}'.format(nome.title(), m))'''
print('Sua média {:.2f}'.format(m))
print('Parabéns' if m>= 6 else 'Estude mais!')
