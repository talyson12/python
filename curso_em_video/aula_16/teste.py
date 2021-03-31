from time import sleep

# ['capital', 'estado']
capitais = ['rio de janeiro', 'RJ', 'belo horizonte', 'MG', 'belém', 'PA', 'curitiba', 'PR']
acertos = erros = 0

nome = str(input('Digite o seu nome: '))
print(f'Bem-vindo, {nome.title()}!')
resposta = ' '
while True:
    resposta = str(input('Vamos jogar? (S/N) ')).strip().lower()[0]
    if resposta not in 'sn':
        print('Resposta inválida!')
    else:
        break
if resposta == 's':
    print('Começando!')
    for capital in range(1, len(capitais), 2):
        resp_aluno = str(input(f'Qual a capital desse estado [{capitais[capital]}]: ')).strip().lower()
        if resp_aluno == capitais[capital - 1]:
            acertos += 1
        else:
            erros += 1
    print('Fim de jogo!')
    sleep(0.5)
    print('Hora dos resultados...')
    sleep(0.5)
    print(f'Seus erros: {erros}\nSeus acertos: {acertos}')
else:
    print('Que pena...')
    sleep(0.5)
    print(':', end='')
    sleep(0.2)
    print('-', end='')
    sleep(0.2)
    print('(', end='')
