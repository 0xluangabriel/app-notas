#imports
import os
import json
#variaveis
try:
     with open ('notas.json', 'r', encoding='utf-8') as abrir:
          notas_usuario = json.load(abrir)
except FileNotFoundError: 
    notas_usuario = {}
#------------------------------------------------------------------
#Iniciar terminal
#Pedir para o usuário escolher uma opção
#Opções: Criar nova nota, editar nota existente, visualizar notas, excluir nota, sair
#------------------------------------------------------------------
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""   
    
                (╬￣皿￣)凸    
                            Escolha uma opção:

                        1. Criar nova nota
                        2. Editar nota existente
                        3. Visualizar notas
                        4. Excluir nota
                        5. Sair                         """)

    input_usuario = int(input('\nDigite a opção desejada: '))
    if input_usuario <= 0 and input_usuario > 6:
        print('Opção inválida.')
         
#------------------------------------------------------------------
#CRIAÇÃO DE NOTAS
    if input_usuario == 1:
        titulo_nota = str(input('Digite o título: '))
        conteudo_nota = str(input('Digite o conteúdo: '))
        notas_usuario[titulo_nota] = conteudo_nota
        with open ('notas.json', 'w', encoding='utf-8') as abrir:
            json.dump(notas_usuario, abrir, ensure_ascii=False, indent=4)
             
#------------------------------------------------------------------
#EDIÇÃO DE NOTAS
    elif input_usuario == 2:
        if len(notas_usuario) == 0:
            print('Não há notas para editar, crie uma!')
            input('\nAperte Enter para voltar ao menu...')
        else:
            for numero_notas, (listar_notas, listar_conteudo) in enumerate(notas_usuario.items(), start=1):
                print('-=-'*15)
                print('{} - Título: {}'.format(numero_notas, listar_notas))
                print('-=-'*15)
                lista_notas = list (notas_usuario.keys())
            try: 
                escolha_edit = int(input('Escolha a nota para editar: '))
            except ValueError:
                print('Digite apenas números: ')
                continue
            if escolha_edit > numero_notas:
                print('Nota inexistente.')
            else:
                novo_conteudo = input('Digite o novo conteúdo da nota: ').strip()
                confirma = input('Confirma? [S/N]: '.upper())
                if confirma == 'S':
                    notas_usuario[lista_notas[escolha_edit-1]] = novo_conteudo
                    with open ('notas.json', 'w', encoding='utf-8') as abrir:
                        json.dump(notas_usuario, abrir, ensure_ascii=False, indent=4)
                elif confirma == 'N':
                     print('Edição cancelada!')
            input('\nAperte Enter para voltar ao menu...')
#------------------------------------------------------------------
#LISTAGEM DE NOTAS
    elif input_usuario == 3:
        if len(notas_usuario) == 0:
            print('Não há notas para mostrar, crie uma!')
        for numero_notas, (listar_notas, listar_conteudo) in enumerate(notas_usuario.items(), start=1):
                    print('-=-'*15)
                    print('{} - Título: {}'.format(numero_notas, listar_notas))
                    print('Conteúdo: {}'.format(listar_conteudo))
                    print('-=-'*15)
        input('\nAperte Enter para voltar ao menu...')
#------------------------------------------------------------------
#EXCLUSÃO DE NOTAS
    elif input_usuario == 4:
        if len(notas_usuario) == 0:
            print('Não há notas para mostrar, crie uma!')
            input('\nAperte Enter para voltar ao menu...')
        else:
            for numero_notas, (listar_notas, listar_conteudo) in enumerate(notas_usuario.items(), start=1):
                            print('-=-'*15)
                            print('{} - Título: {}'.format(numero_notas, listar_notas))
                            print('-=-'*15)
            lista_notas = list (notas_usuario.keys())
            try:
                escolha_delete = int(input('Digite o número da nota para apagar: '))
            except ValueError:
                print('Digite apenas números.')
                continue
            if escolha_delete > numero_notas:
                print('Nota inexistente.')
            else:
                    confirma = str(input('Confirma? [S/N]: ').upper())
                    if confirma == 'S':
                        notas_usuario.pop(lista_notas[escolha_delete-1])
                    elif confirma == 'N':
                        print('Exclusão cancelada!')
                    with open ('notas.json', 'w', encoding='utf-8') as abrir:
                        json.dump(notas_usuario, abrir, ensure_ascii=False, indent=4)
            input('\nAperte Enter para voltar ao menu...')
#------------------------------------------------------------------
#ADEUS!
    elif input_usuario == 5:
        print('Tchauzinho!')
        break
    else:
        print('Opção/Entrada errada.')
        input('\nAperte Enter para voltar ao menu...')
#------------------------------------------------------------------
