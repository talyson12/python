r1 = float(input('Digite o valor do l1: '))
r2 = float(input('Digite o valor do l2: '))
r3 = float(input('Digite o valor do l3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo!')
