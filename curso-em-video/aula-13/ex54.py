from datetime import date
dataAtual = date.today().year
maior = 0
for c in range(0, 7):
    nasci = int(input('Digite o seu ano de nascimento: '))
    if dataAtual - nasci >= 21:
        maior += 1
print('Maiores de idade:', maior)
print('Menores de idade:', 7 - maior)