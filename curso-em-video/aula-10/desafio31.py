km = float(input('Quantos km é a sua viagem? '))
'''if km <= 200:
    print('Você vai pagar R${:^10.2f}!'.format(km * 0.5))
else:
    print('Você vai pagar R$ {:.2f}'.format(km * 0.45))
'''
preco = km * 0.5 if km <= 200 else km * 0.45
print('O preço da sua passageme é: R$ {:^10.2f}'.format(preco))
