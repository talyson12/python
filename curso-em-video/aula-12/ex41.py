from datetime import date
nasci = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
if anoAtual - nasci <= 9:
    resp = 'MIRIM'
elif 9 < anoAtual - nasci <= 14:
    resp = 'INFANTIL'
elif 14 < anoAtual - nasci <= 19:
    resp = 'JUNIOR'
elif anoAtual - nasci == 20:
    resp = 'SÊNIOR'
else:
    resp = 'MASTER'
print(resp)
#print(date.today().year)
