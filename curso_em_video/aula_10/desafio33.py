a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

'''lista =[a, b, c]
lista_ordenada = sorted(lista)
print('O menor número é', lista_ordenada[0])
print ('O maior número é', lista_ordenada[2])'''

'''lista = [a, b, c]
print('O maior valor digitado foi {}'.format(max(lista)))
print('O menor numero digitado foi {}'.format(min(lista)))'''

#menor ok
menor = a
if b < a and b < a:
    menor = b
if c < a and c < b:
    menor = c
print('O menor é:', menor)
#maior ok
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O maior é:', maior)
