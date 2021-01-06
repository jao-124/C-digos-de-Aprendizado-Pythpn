def insere_atividade():
    n = input('insira o numero de atividades a serem cadastradas: ')

    # atividade = {'titulo': 't', 'materia': 'm', 'pontuação': 'p', 'data': 'd' }
    i = int(n)
    lista = list()
    while i > 0:
        lista.append({'título': input('Insira o título da atividade: '), 'materia': input('Insira a materia: '),
                      'pontuacao': int(input('Insira a pontuacao: ')), 'data': input('Insira a data de entrega: ')})
        i -= 1
    lista_ordenada = sorted(lista, key=lambda k: k['pontuacao'], reverse=True)
    with open('Lista_atividades', 'a+') as file:
        for n in range(len(lista_ordenada)):
            file.writelines(str(lista_ordenada[n]).split(sep=',{'))
            file.write('\n')
#file.writelines(str(lista_ordenada).split(sep=',{'))
    return lista_ordenada


def deleta_atividade(lista):
    n = input('Entre com a posição, entre espaços, das atividades a eliminar da lista: ')
    leng = n.split()
    t = len(leng)
    i = t
    while i > 0:
        i -= 1
        del (lista[int(leng[i])])

    with open('Lista_atividades', 'w+') as file:
        for n in range(len(lista)):
            if str(lista[n]) != '\n':
                file.writelines(str(lista[n]).split(sep=',{'))
#              file.write('\n')


def imprime_atividade():
    file = open('Lista_atividades')
    print(file.read())



p = True
while p is True:
    arquivo = open('Lista_atividades')
    lista_univ = arquivo.readlines()
    c = input(
        'Entre com uma opção de execução:\n[1] - Inserir atividade\n[2] - Deletar atividade\n[3] - Imprimir lista de '
        'tarefas\n[4] - Sair\n')
    if int(c) == 1:
        lista_univ = insere_atividade()
    if int(c) == 2:
        deleta_atividade(lista_univ)
    if int(c) == 3:
        imprime_atividade()
    if int(c) == 4:
        p = False
