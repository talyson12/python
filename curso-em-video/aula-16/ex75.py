tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
pares = 0
cont3 = 0
for c in tupla:
    if c % 2 == 0 and c != 0:
        pares += 1
print(f'O valor 9 foi digitado {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 foi digitado na {tupla.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado')
if pares == 4:
    print(f'Os valores pares foram {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]}')
else:
    print(f'Foram digitados {pares} pares')
