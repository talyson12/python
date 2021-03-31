homens = maiorIdade = menorMulher = 0
while True:
    idade = - 1
    while idade < 0:
        idade = int(input('Qual a sua idade: '))
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Qual o seu séxo (F/M): ')).strip().lower()[0]
    if sexo == 'm':
        homens += 1
    if idade >= 18:
        maiorIdade += 1
    if sexo == 'f' and idade < 20:
        menorMulher += 1
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar (SIM/NÃO)? ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'''Maiores de idade: {maiorIdade}
Total de homens: {homens}
Mulheres menores de 20 anos: {menorMulher}''')
