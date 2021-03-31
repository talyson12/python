num = int(input('Digite um número: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        div += 1
if div == 2:
    print(f'O número {num} é primo.')
