mIdade = 0
velho = 0
Nvelho = '[vazio]'
Nnovas = 0
for c in range(0, 4):
    nome = str(input('Digite o seu nome: ')).strip().lower().title()
    sexo = str(input('Seu sexo (M/F): ')).strip().lower()
    idade = int(input('Sua idade: '))
    mIdade += idade
    if sexo == 'm':
        if idade > velho:
            Nvelho = nome
    else:
        if idade < 20:
            Nnovas += 1
print(f'''A média das idades é: {mIdade / 4}
O nome do homem mais velho é: {Nvelho}
Quantas mulheres tem menos que 20 anos: {Nnovas}''')
