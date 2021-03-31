frase = 'Curso em Vídeo Python'
print(len(frase)) #comprimento do caractere
print(frase.count('o', 0, 13)) #de 0 até 0 13 quantos 'o'
print(frase.count('o')) #quantas letras 'o' tem na string
print(frase.upper().count('O')) #coloco a frase em maiúsculo e conto quantas letras 'O' tem
print(frase.lower().count('c')) #mesma coisa só que em minúsculo
print(len(frase)) #tamanho da string, incluindo espaços
print(frase.replace('Python', 'Android')) #trocar python por android
print(frase.capitalize()) #só o primeiro caractere fica maiúsculo, da frase inteira
print(frase.title()) #a primeira letra de cada palavra em maiúsculo
print('Curso' in frase) #se 'Curso' está na frase
print(frase.find('Curso')) #mostra onde começa 'Curso'
print(frase.lower().find('vídeo'))
print(frase.split()) #pego as palavras da frase e coloco em uma lista
divido = frase.split()
print(divido[2])
print(divido[2][3]) #pega palavra 2 e mostre a letra 3
print('-'.join(frase)) #junto os elementos de frase e separo com '-'
fraseDois = '   Curso em   Vídeo '
print(fraseDois,'\n', frase.strip()) #tira os espaços início e fim; frase.rstrip() e frase.lstrip() tira os espaços right e left
