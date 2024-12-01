value = input('Digite um valor qualquer: ')

print(f'==== Sobre {value} ====')
print('É um número:', value.isnumeric())
print('É uma letra:', value.isalpha())
print('É um alfanumérico:', value.isalnum())
print('É um número decimal:', value.isdecimal())
print('É a tecla espaço:', value.isspace())
