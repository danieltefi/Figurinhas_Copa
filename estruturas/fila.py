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