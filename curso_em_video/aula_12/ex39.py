from datetime import date
nasci = int(input('Informe o seu ano da nascimento: '))
if date.today().year - nasci < 18:
    temp = 18 - (date.today().year - nasci)
    print(f'Ainda terá que se alistar, faltam {temp} ano(s)\nVocê vai se alistar em {18 - (date.today().year - nasci) + date.today().year}')
    resp = ''
elif date.today().year - nasci == 0:
    resp = 'Está na hora de se alistar.'
else:
    temp = (date.today().year - nasci) - 18
    print(f'Você está {temp} ano(s) atrasado, seu alistamento era em {nasci + 18}!')
    resp = ''
print(resp)
