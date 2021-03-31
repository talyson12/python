nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if (nota1 + nota2) / 2 < 5:
    print('Reprovado')
elif 5 <= (nota1 + nota2) / 2 < 7:
    print('Recuperação')
    resp = str(input('Você fez a recuperação (S / N): ')).strip().lower()
    if resp == 's':
        nota3 = float(input('Digite sua nota recuperação: '))
        if (((nota1 + nota2) / 2) + nota3) / 2 >= 7:
            print('Aprovado')
        else:
            print('Reprovado')
    else:
        print('Reprovado')
else:
    print('Aprovado')
