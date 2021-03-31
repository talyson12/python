num = int(input('Digite um número: '))
cover = int(input('Gostaria de converter em: \n[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\nSua opçaõ: '))
if cover == 1:
    print(f'{num} em binário é:', bin(num)[2:])
elif cover == 2:
    print(f'{num} em Octal é:', oct(num)[2:])
elif cover == 3:
    print(f'{num} em Hexadecimal é:', hex(num)[2:])
else:
    print('Opção inválida!')
