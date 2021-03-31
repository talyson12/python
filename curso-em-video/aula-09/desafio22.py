nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculo:', nome.upper())
print('Seu nome em minúsculo:', nome.lower())
print('Seu nome tem ao todo: {} letras'.format(len(nome) - nome.count(' ')))
primeiroSeparado = nome.split()
print('Seu primeiro nome tem:', len(primeiroSeparado[0]),
'letras')
#outro jeito é usando nome.find(' ')
