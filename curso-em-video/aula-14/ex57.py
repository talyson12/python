sexo = str(input('Digite o seu sexo (M/F): ')).strip().lower()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido, digite novamente: ')).strip().lower()[0]
print('ACABOU')
