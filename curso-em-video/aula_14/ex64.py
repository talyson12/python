soma = c = 0
num = int(input('Digite um número: '))
while num != 999:
    c += 1
    soma += num
    num = int(input('Digite um número: '))
print(f'A soma entre eles é {soma} e foram digitados {c} números')
