#cores no terminal
'''print('\033[1:31:43mOlá, mundo!\033[m') #padrao \033[codigom 1 style negrito para texto 31 > vermelho para texto e 43 amarelo para fundo
print('\033[7:33:44mMá, oie!\033[m') #7 vai inventer as cores entre fundo e texto
a = 2
b = 3
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}')
#32 cor verde {texto} e 33 vermelho {texto}'''

nome = 'Talyson'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretobranco':'\033[7:30m'
}
print('Olá, prazer em te conhecer, {} {} {}!'.format(cores['pretobranco'], nome, cores['limpa']))
