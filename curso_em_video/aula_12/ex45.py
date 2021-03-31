from random import randint
from time import sleep
# 0 == pedra
# 1 == tesoura
# 2 == papel
máquina = randint(0, 2)
print('-=' * 12)
print('Jogo pedra papel tesoura')
print('-=' * 12)
sleep(0)
print('Escolha seu mão!')
jogador = int(input('[ 0 ] == pedra\n[ 1 ] == tesoura\n[ 2 ] == papel\n'))
if máquina == jogador:
    resp = 'Empate!'
elif máquina == 2 and jogador == 0:
    resp = 'Você perdeu!'
elif máquina == 0 and jogador == 1:
    resp = 'Você perdeu!'
elif máquina == 1 and jogador == 2:
    resp = 'Você perdeu!'
elif jogador == 2 and máquina == 0:
    resp = 'Você venceu!'
elif jogador == 0 and máquina == 1:
    resp = 'Você venceu!'
else:
    resp = 'Você venceu!'
sleep(0)
print('Máquina escolhendo!')
sleep(1)
print('...')
sleep(1)
print(f'Resultado: {resp}\nMáquina: {máquina}\nVocê: {jogador}')

