from random import randint
computador = randint(0, 10)
cont = 1
jogador = int(input('Digite um número: '))
if jogador != computador:
    while jogador != computador:
        jogador = int(input('Você errou, tente novamente: '))
        cont += 1
    print('\033[33mACERTOU!\033[m Mas precisou de {} tentativas'.format(cont))
else:
    print('Você acertou \033[34macertou!\033[m')
