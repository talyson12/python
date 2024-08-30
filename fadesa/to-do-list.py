escolha = int(input('======= ToDoList =======\n1 - Adicionar uma tarefa\n2 - Mostrar tarefas\n3 - Excluir taredas\n4 - Sair\n'))


# primeiro passo, verificar se a opção digitada é válida: verifico se o que foi digitado foi um número, depois verificar se foi um número válido
if escolha.isnumeric(): # verifica se foi um número ou não
    escolha = int(escolha)
    if escolha > 0 and escolha < 5 and (escolha % 1 == 0): # verifica se foi um número válido 
        print('OK')
    else:
        print('NOK')
else:
    print('NOK')

