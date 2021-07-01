n = int(input('Digite o valor do saque: '))
cont = contOriginal = n
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = 0
while cont // 100 > 0:
    nota100 += 1
    cont -= 100
print(f'Será possível imprimir {nota100} nota(s) de R$ 100,00')
while cont // 50 > 0:
    nota50 += 1
    cont -= 50
print(f'Será possível imprimir {nota50} nota(s) de R$ 50,00')
while cont // 20 > 0:
    nota20 += 1
    cont -= 20
print(f'Será possível imprimir {nota20} nota(s) de R$ 20,00')
while cont // 10 > 0:
    nota10 += 1
    cont -= 10
print(f'Será possível imprimir {nota5} nota(s) de R$ 10,00')
while cont // 5 > 0:
    nota5 += 1
    cont -= 5
print(f'Será possível imprimir {nota5} nota(s) de R$ 5,00')
while cont // 2 > 0:
    nota2 += 1
    cont -= 2
print(f'Será possível imprimir {nota2} nota(s) de R$ 2,00')
