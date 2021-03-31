num1 = float(input('Digite um número: '))
print('O número {:-^10} em centímetros é: {:-<2}\nE em milímetros é: {:->2}'.format(num1, num1*100, num1*1000))