preco = float(input('Digite o preço do produto: '))
pagamento = int(input('Digite a forma de pagamento (0 (avista), 1 (cartão avista) ou + número de prestações: '))
if pagamento == 0:
    preco = preco * 0.9
elif pagamento == 1:
    preco = preco * 0.95
elif pagamento == 2:
    preco = preco / 2
else:
    preco = preco * 1.2 / pagamento
print('Você irá pagar: R$ {:.2f}'.format(preco))
print('{:=^20}'.format('bolsonaro'))
