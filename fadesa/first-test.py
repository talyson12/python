# print('ola')

''' nome = input('Escreva seu nome ')
# '+' só pode concatenar strings
print('Seu nome é ' + nome + '!')
sobreNome = input('Digite seu sobrenome: ')

print('olá, {} {}!'.format(nome, sobreNome))
print(f'olá {nome} {sobreNome}') '''

# o input sempre retorna uma string. portanto, para fazer manipulações matemáticas, será necessário converter usando int(variavel)
''' idade = int(input('Digite sua idade: '))
print('Sua idade + 2 é:', idade + 2) '''

''' :-^10: O número será centralizado (^) dentro de um campo de 10 caracteres de largura, e os espaços restantes serão preenchidos com o caractere -.
:-<2: O valor será alinhado à esquerda (<) dentro de um campo de 2 caracteres de largura, e qualquer espaço restante será preenchido com o caractere -.
:->2: O valor será alinhado à direita (>) dentro de um campo de 2 caracteres de largura, e os espaços à esquerda serão preenchidos com o caractere -. ''' 
''' num1 = int(input('Digite um número: '))
print('O número {:-^10} em centímetros é: {:-<10}\nE em milímetros é: {:->10}'.format(num1, num1*100, num1*1000)) '''

# end adiciona '>>' no final da linha e o que eu pedir pra imprimir depois continuará na mesma linha
print('ola mundo 2 ', end='>>>')
print(' sacou?')



