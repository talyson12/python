num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 == num2:
    resp = 'Os dois números são \033[1:36miguais\033[m!'
elif num1 > num2:
    resp = 'O número 1 é \033[1:34mmaior\033[m!'
else:
    resp = 'O número 2 é \033[1:31mmaior\033[m!'
print(resp)
