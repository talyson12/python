l1 = int(input('Digite o lado L1: '))
l2 = int(input('Digite o lado L2: '))
l3 = int(input('Digite o lado L3: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    resp = 'Sim, pode formar um triângulo.'
    if (l1 == l2 and l1 != l3) or (l1 == l3 and l2 != l3) or (l2 == l3 and l2 != l1):
        resp2 = 'Triângulo isóceles.'
    elif l1 == l2 == l3:
        resp2 = 'Triângulo equilátero.'
    else:
        resp2 = 'Triângulo escaleno.'
else:
    resp = 'Não, não pode formar um triângulo'
    resp2 = ''
print(resp, resp2)
