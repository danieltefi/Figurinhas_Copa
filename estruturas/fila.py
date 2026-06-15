from modelos.nodos import NodoFila

class Fila:
    def __init__(self):
        self.inicio = None  # primeiro elemento da fila 
        self.fim = None     # último elemento da fila 

    def enqueue(self, nova_figurinha):  # coloca no final da fila
        novo_nodo = NodoFila(nova_figurinha)

        # Se a fila estiver vazia, novo nó é início e fim ao mesmo tempo
        if self.inicio is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo # atual último aponta pro novo, e o fim muda pro novo nó
            self.fim = novo_nodo

    def dequeue(self):  # remove do início da fila e retorna figurinha
        if self.inicio is None: # se fila estiver vazia, não tem o que remover
            return None

        figurinha_removida = self.inicio.figurinha # salva figurinha que vai sair para poder retornar no final
        
        self.inicio = self.inicio.proximo # início anda pro próximo nó da fila

        if self.inicio is None: # se depois de andar a fila ficou vazia, fim também vira none
            self.fim = None

        return figurinha_removida

    def peek(self):  # apenas espia o primeiro da fila, sem remover
        if self.inicio is None:
            return None
        return self.inicio.figurinha

    def limpar(self):  # esvazia fila inteira
        self.inicio = None
        self.fim = None

    def processar_proxima_troca(self, album_principal, album_repetidas, fila_historico):
        figurinha_proposta = self.peek() # espia primeira proposta da fila
        
        if figurinha_proposta is None:
            print('Não há propostas de troca na fila.')
            return False

        tem_repetida = album_repetidas.buscar_por_id(figurinha_proposta.id) # verifica se há essa figurinha nas repetidas

        if tem_repetida is not None:
            fig_recebida = self.dequeue() # se temos a repetida, aceita a troca e tira proposta da fila
            
            album_repetidas.remover(figurinha_proposta.id) # tira a figurinha do álbum de repetidas
            
            album_principal.pacotinho_inserir_figurinha(fig_recebida, album_repetidas) # tenta colar no álbum principal (se for repetida, vai para as repetidas)
            
            fila_historico.enqueue(fig_recebida) # guarda no histórico
            
            print(f'Troca efetuada! Trocada a repetida do {figurinha_proposta.nome}.')
            return True
        else:
            print(f'Você não tem a figurinha #{figurinha_proposta.id} repetida para fazer essa troca.')
            return False