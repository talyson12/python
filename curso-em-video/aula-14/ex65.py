resp = 's'
média = cont = maior = menor = 0
while resp == 's':
    cont += 1
    num = int(input('Digite um número: '))
    média += num
    resp = str(input('Quer continuar? (S/N): ')).strip().lower()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'''A média aritmética entre os termos é {média / cont};
O maior e menor entre eles é {maior} e {menor}''')
