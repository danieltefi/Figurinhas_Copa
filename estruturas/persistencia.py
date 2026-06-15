import json
import os
from modelos.figurinha import Figurinha

def salvar_dados(caminho_arquivo, album_principal, album_repetidas, fila_trocas, fila_historico):
    dados_para_salvar = { # cria estrutura básica pra organizar dados em formato de texto
        "album": [],
        "repetidas": [],
        "trocas": [],
        "historico": []
    }

    atual = album_principal.cabeca # varre álbum principal nó por nó e guarda dados das figurinhas
    while atual is not None:
        dados_fig = {
            "id": atual.figurinha.id,
            "nome": atual.figurinha.nome,
            "pais": atual.figurinha.pais,
            "raridade": atual.figurinha.raridade
        }
        dados_para_salvar['album'].append(dados_fig)
        atual = atual.proximo

    atual_rep = album_repetidas.cabeca # varre álbum de repetidas nó por nó
    while atual_rep is not None:
        dados_fig = {
            "id": atual_rep.figurinha.id,
            "nome": atual_rep.figurinha.nome,
            "pais": atual_rep.figurinha.pais,
            "raridade": atual_rep.figurinha.raridade
        }
        dados_para_salvar['repetidas'].append(dados_fig)
        atual_rep = atual_rep.proximo

    atual_fila = fila_trocas.inicio # varre fila de trocas
    while atual_fila is not None:
        dados_fig = {
            "id": atual_fila.figurinha.id,
            "nome": atual_fila.figurinha.nome,
            "pais": atual_fila.figurinha.pais,
            "raridade": atual_fila.figurinha.raridade
        }
        dados_para_salvar['trocas'].append(dados_fig)
        atual_fila = atual_fila.proximo

    atual_hist = fila_historico.inicio # varre fila histórico
    while atual_hist is not None:
        dados_fig = {
            "id": atual_hist.figurinha.id,
            "nome": atual_hist.figurinha.nome,
            "pais": atual_hist.figurinha.pais,
            "raridade": atual_hist.figurinha.raridade
        }
        dados_para_salvar['historico'].append(dados_fig)
        atual_hist = atual_hist.proximo

    arquivo = open(caminho_arquivo, 'w', encoding='utf-8') # grava dicionário estruturado dentro do arquivo JSON
    json.dump(dados_para_salvar, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()


def carregar_dados(caminho_arquivo, album_principal, album_repetidas, fila_trocas, fila_historico):
    if not os.path.exists(caminho_arquivo): # se arquivo não existir (primeira vez rodando o sistema), não faz nada
        return

    arquivo = open(caminho_arquivo, 'r', encoding='utf-8') # abre o arquivo
    dados_carregados = json.load(arquivo)
    arquivo.close()

    if 'album' in dados_carregados:
        for dados in dados_carregados['album']: # reconstrói álbum principal
            nova_fig = Figurinha(dados['id'], dados['nome'], dados['pais'], dados['raridade'])
            album_principal.adicionar(nova_fig)

    if 'repetidas' in dados_carregados:
        for dados in dados_carregados['repetidas']: # reconstrói repetidas
            nova_fig = Figurinha(dados['id'], dados['nome'], dados['pais'], dados['raridade'])
            album_repetidas.adicionar(nova_fig)

    if 'trocas' in dados_carregados:
        for dados in dados_carregados['trocas']: # reconstrói fila de trocas
            nova_fig = Figurinha(dados['id'], dados['nome'], dados['pais'], dados['raridade'])
            fila_trocas.enqueue(nova_fig)

    if "historico" in dados_carregados:
        for dados in dados_carregados['historico']: # reconstrói fila histórico
            nova_fig = Figurinha(dados['id'], dados['nome'], dados['pais'], dados['raridade'])
            fila_historico.enqueue(nova_fig)