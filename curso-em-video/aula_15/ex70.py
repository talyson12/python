soma = maisBarato = maisCaro = cont = 0
nomeBarato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = int(input('Digite o preço do produto: '))
    soma += preço
    cont += 1
    if preço > 1000:
        maisCaro += 1
    if cont == 1 or preço < maisBarato:
        maisBarato = preço
        nomeBarato = nome
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? (SIM/NÃO) ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'''Total gasto: {soma}
Produtos que custam mais de 1000 reais: {maisCaro}
Nome do produto maias barato: {nomeBarato}, preço {maisBarato}''')
