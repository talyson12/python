from math import pow
h = float(input('Digite a sua altura (n): '))
p = float(input('Digite o seu peso (kg): '))
if p / pow(h, 2) > 40:
    resp = 'Obesidade mórbida.'
elif 30 < p / pow(h, 2) <= 40:
    resp = 'Obesidade.'
elif 25 < p / pow(h, 2) <= 30:
    resp = 'Sobrepeso.'
elif 18.5 < p / pow(h, 2) <= 25:
    resp = 'Peso ideal.'
else:
    resp = 'Abaixo do peso.'
print(resp)
