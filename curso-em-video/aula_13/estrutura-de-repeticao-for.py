'''for c in range(6, 0, -2): 5 vezes, no 6 ele para, não faz ele
    print(c)'''

'''n = int(input('Digite um número: '))
passo = int(input('Digite o passo: '))
if passo > 0:
    for c in range(0, n + 1, passo):
        print(c, end=' > ')
else:
    for c in range(n, -1, passo):
        print(c, end=' > ')'''

nome = str(input('Digite o seu nome completo: ')).strip().title().split()
quantidade = len(nome)
for c in range(0, quantidade):
    print(nome[c], end=' ')
print('\nFIM')
