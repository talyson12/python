frase = input('Digite uma frase: ').strip()
print('Quantas vezes a letra A aparece:', frase.lower().count('a'))
print('Em qual posição ela aparece a primeira vez:', frase.lower().find('a') + 1)
print('Em qual posição ela aparece a última vez:', frase.lower().rfind('a') + 1)

