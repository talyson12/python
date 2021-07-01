mult = 0
quant = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        mult += c
        quant += 1
print(f'A soma deles é {quant} é {mult}')