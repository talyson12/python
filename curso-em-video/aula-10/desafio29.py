vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    mult = (vel - 80) * 7
    print('Acima da média, você terá que pegar uma multa de R$ {:.2f}'.format(mult))
print('Está no limite permitido.')
