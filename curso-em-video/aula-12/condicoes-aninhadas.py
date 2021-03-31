nome = str(input('Digite o seu nome: ')).lower().strip()
if nome == 'talyson':
    print('Que nome bonito!')
#elif nome == 'andré' or nome =='alves':
#    print('Nome muito bonito também!')
elif nome in 'andré alves':
    print('Nome daora, parça')
print(f'Tenha um ótimo dia, {nome}!')
