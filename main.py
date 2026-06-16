import os
import subprocess
from modelos.figurinha import Figurinha
from estruturas.album import Album
from estruturas.fila import Fila
from estruturas.persistencia import salvar_dados, carregar_dados

def limpar_tela(): # limpa terminal para ficar legível
    if os.name == 'nt':
        subprocess.run('cls', shell=True)    # se for windows, usa cls
    else:
        subprocess.run('clear', shell=True)  # Se for linux ou mac, usa clear

def exibir_menu():
    print('\n' + '='*40)
    print('ÁLBUM VIRTUAL - COPA DO MUNDO 2026')
    print('='*40)
    print('1  - Inserir Figurinha')
    print('2  - Ver Álbum Completo')
    print('3  - Ver Figurinhas Repetidas')
    print('4  - Remover Figurinha do Álbum')
    print('5  - Buscar Figurinha')
    print('6  - Ver Porcentagem Concluída')
    print('7  - Criar Proposta de Troca')
    print('8  - Processar Próxima Troca da Fila')
    print('9  - Ver Histórico de Trocas')
    print('0  - Salvar e Sair')
    print('='*40)

def main():
    caminho_json = 'dados/dados_album.json' # caminho onde dados serão salvos localmente

    pasta_dados = os.path.dirname(caminho_json) # extrai o nome da pasta (que é 'dados')
    if pasta_dados: # garante que a pasta 'dados' exista
        os.makedirs(pasta_dados, exist_ok=True) # se a pasta não existir, o os.makedirs cria automaticamente, exist_ok=True serve para não dar erro caso pasta já exista
    
    TOTAL_FIGURINHAS_ALBUM = 20 # define tamanho total que álbum terá (20 figurinhas de teste)

    meu_album = Album() # cria estruturas dinâmicas que gerenciam os nós
    minhas_repetidas = Album()  # repetidas usam estrutura do álbum pra ficarem ordenadas por id
    fila_propostas = Fila()
    historico_trocas = Fila()

    carregar_dados(caminho_json, meu_album, minhas_repetidas, fila_propostas, historico_trocas) # carrega dados salvos no JSON (se houver)
    rodando = True
    while rodando:
        limpar_tela()
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            print('\n--- INSERIR NOVA FIGURINHA ---')
            try:
                id_fig = int(input('Digite o número (ID) da figurinha: ').strip())
                nome = input('Digite o nome do jogador: ').title()
                pais = input('Digite o país/seleção: ').title()
                raridade = input('Digite a raridade (vazio para comum): ').lower()

                nova_fig = Figurinha(id_fig, nome, pais, raridade) # cria objeto figurinha
                
                meu_album.pacotinho_inserir_figurinha(nova_fig, minhas_repetidas) # executa lógica de negócio automática (álbum ou repetidas)
            except ValueError:
                print('Erro: O ID da figurinha deve ser um número inteiro válido.')
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '2':
            print('\n--- SEU ÁLBUM DE FIGURINHAS ---')
            if meu_album.cabeca is None:
                print('Seu álbum ainda está totalmente vazio.')
            else:
                atual = meu_album.cabeca
                while atual is not None:
                    print(atual.figurinha)
                    atual = atual.proximo
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '3':
            print('\n--- SUAS FIGURINHAS REPETIDAS ---')
            if minhas_repetidas.cabeca is None:
                print('Você não tem nenhuma figurinha repetida ainda.')
            else:
                atual = minhas_repetidas.cabeca
                while atual is not None:
                    print(atual.figurinha)
                    atual = atual.proximo
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '4':
            print('\n--- REMOVER FIGURINHA ---')
            try:
                id_para_remover = int(input('Digite o ID da figurinha que deseja descolar: ').strip())
                removeu = meu_album.remover(id_para_remover)
                if removeu:
                    print(f'Figurinha #{id_para_remover} removida do álbum.')
                else:
                    print(f'Figurinha #{id_para_remover} não foi encontrada no seu álbum.')
            except ValueError:
                print('Erro: Por favor, digite um número válido.')
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '5':
            print('\n--- BUSCAR FIGURINHA ---')
            print('1 - Buscar por Número (ID)')
            print('2 - Buscar por Nome do Jogador')
            print('3 - Buscar por Seleção (País)')
            sub_opcao = input('Escolha o tipo de busca: ')

            if sub_opcao == '1':
                try:
                    id_busca = int(input('Digite o ID: ').strip())
                    res = meu_album.buscar_por_id(id_busca)
                    if res is not None:
                        print(f'Encontrada no Álbum: {res}')
                    else:
                        print('Figurinha não encontrada no álbum.')
                except ValueError:
                    print('Erro: ID inválido.')

            elif sub_opcao == '2':
                nome_busca = input('Digite o nome completo do jogador: ').title()
                res = meu_album.buscar_por_jogador(nome_busca)
                if res is not None:
                    print(f'Encontrada no Álbum: {res}')
                else:
                    print('Jogador não encontrado no álbum.')

            elif sub_opcao == '3':
                pais_busca = input('Digite o nome do país: ').title()
                print(f'\nBuscando figurinhas da seleção ({pais_busca}):')
                meu_album.buscar_por_selecao(pais_busca)

            else:
                print('Opção de busca inválida.')
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '6':
            print('\n--- PROGRESSO DO ÁLBUM ---')
            porcentagem = meu_album.calcular_porcentagem(TOTAL_FIGURINHAS_ALBUM)
            print(f'Você possui {meu_album.tamanho} de {TOTAL_FIGURINHAS_ALBUM} figurinhas únicas.')
            print(f'Seu álbum está {porcentagem:.2f}% concluído!')
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '7':
            print('\n--- REGISTRAR PROPOSTA DE TROCA ---')
            print('Insira os dados da figurinha que estão te oferecendo:')
            try:
                id_fig = int(input('Digite o ID da figurinha: ').strip())
                nome = input('Digite o nome do jogador: ').title()
                pais = input('Digite o país/seleção: ').title()
                raridade = input('Digite a raridade (se houver): ').lower()

                fig_proposta = Figurinha(id_fig, nome, pais, raridade)
                fila_propostas.enqueue(fig_proposta)
                print(f'Proposta com a figurinha do {nome} adicionada à fila de espera.')
            except ValueError:
                print('Erro: Dados de entrada incorretos.')
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '8':
            print('\n--- PROCESSANDO TROCA AUTOMÁTICA ---')
            fila_propostas.processar_proxima_troca(meu_album, minhas_repetidas, historico_trocas) # executa método de negócio contido na classe fila
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '9':
            print('\n--- HISTÓRICO DE TROCAS REALIZADAS ---')
            if historico_trocas.inicio is None:
                print('Nenhuma troca foi realizada até o momento.')
            else:
                atual = historico_trocas.inicio
                contador = 1
                while atual is not None:
                    print(f'{contador}. Você recebeu: {atual.figurinha}')
                    atual = atual.proximo
                    contador = contador + 1
            input('\nPressione enter para voltar ao menu...')

        elif opcao == '0':
            print('\nSalvando dados e fechando sistema de figurinhas...')
            salvar_dados(caminho_json, meu_album, minhas_repetidas, fila_propostas, historico_trocas)
            print('Dados gerados.')
            rodando = False

        else:
            print('Opção inválida! Tente novamente.')
            input('\nPressione enter para voltar ao menu...')

if __name__ == '__main__':
    main()