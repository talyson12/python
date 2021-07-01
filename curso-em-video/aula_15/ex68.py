'''valor  = 0
while True:
    número = int(input('Digite um número: '))
    if número % 2 != 0:
        valor = 1 #ímpar
    else:
        valor = 2 #par
    resp = str(input('É ímpar ou par: ')).strip().lower()[0]
    if ((resp == 'í' or resp == 'i') and valor == 1) or (resp == 'p' and valor == 2):
        print('Você Acertou!')
    else:
        print('Você errou.')
        break
print('Fim de jogo.')'''

from random import randint
computador = randint(0, 10)
cont = 0
while True:
    num = int(input('Digite um número: '))
    resp = ' '
    while resp not in 'pi': #enquanto resp não estiver em pi faça
        resp = str(input('Você quer PAR ou ÍMPAR? ')).strip().lower()[0]
    if ((num + computador) % 2 == 0) and resp == 'p':
        print(f'''Você Acertou!
A soma deu {num + computador} e o resultado foi PAR''')
        cont += 1
    elif ((num + computador) % 2 != 0) and (resp == 'i' or resp == 'í'):
        print(f'''Você Acertou!
A soma deu {num + computador} e o resultado foi ÍMPAR''')
        cont += 1
    else:
        if (num + computador) % 2 == 0:
            print(f'''Você Perdeu!
A soma foi {num  + computador} e o resultado é PAR''')
        else:
            print(f'''Você perdeu!
A soma foi {num + computador} e o resultado foi ÍMPAR''')
        break
print('Fim de jogo.\nTotal de vitórias:', cont)
