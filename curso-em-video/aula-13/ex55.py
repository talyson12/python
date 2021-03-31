Pmaior = 0
#Pmenor = 99999
Pmenor = 0
for c in range(0, 5):
    peso = float(input('Digite a sua massa corporal (kg): '))
    '''if peso > Pmaior:
        Pmaior = peso
    if peso < Pmenor:
        Pmenor = peso'''
    if c == 1:
        Pmaior = peso
        Pmenor = peso
    else:
        if peso > Pmaior:
            Pmaior = peso
        if peso < Pmenor:
            Pmenor = peso
print(f'O maior e o menor peso foram: {Pmaior}kg, {Pmenor}kg')
