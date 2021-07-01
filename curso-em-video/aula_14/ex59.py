from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
op = int(1)
while op != 5:
    op = int(input('''Qual operação você gostaria de fazer?
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair
    --> '''))
    if op == 1:
        print('A soma é {}'.format(num1 + num2))
        sleep(1)
    elif op == 2:
        print('A multiplicação é {}'.format(num1 * num2))
        sleep(1)
    elif op == 3:
        if num1 != num2:
            if num1 > num2:
                print(f'{num1} é maior que {num2}')
            elif num1 < num2:
                print(f'{num2} é maior que {num1}')
        else:
            print(f'Os números {num1} e {num2} são iguais')
        sleep(1)
    elif op == 4:
        num1 = int(input('Digite o novo número: '))
        num2 = int(input('Digite o outro novo número: '))
        sleep(1)
    else:
        print('saindo', end='')
        for c in range(0, 3):
            print('.',end='')
            sleep(0.5)
print('\nlogout')
