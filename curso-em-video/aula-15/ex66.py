cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados  {cont} números e sua soma foi {soma}')
