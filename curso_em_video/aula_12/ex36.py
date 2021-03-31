preco = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
tempo = int(input('Quanto tempo: '))
tempo = tempo * 12
if preco / tempo > 0.3 * salario:
    print('Infelizmente você \033[31mnão pode\033[m comprar a casa.', end='')
else:
    print('Você \033[32mpode\033[m comprar a casa.', end='')
print(' fim')
