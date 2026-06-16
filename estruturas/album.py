from modelos.nodos import NodoLista

class Album:
    def __init__(self):
        self.cabeca = None # início da lista começa vazio
        self.tamanho = 0 # contador de figurinhas no álbum 

    def adicionar(self, nova_figurinha): # cria um novo nó com a figurinha dentro
        if self.buscar_por_id(nova_figurinha.id) is not None: # garante que ids duplicados nunca passem para os ponteiros abaixo
            return False # retorna false pra avisar que é repetida
        
        novo_nodo = NodoLista(nova_figurinha)

        if self.cabeca is None: # álbum está vazio
            self.cabeca = novo_nodo
            self.tamanho = self.tamanho + 1
            return True # retorna true indicando que foi adicionada com sucesso

        if nova_figurinha.id < self.cabeca.figurinha.id: # nova figurinha tem id menor que a primeira da lista
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
            self.tamanho = self.tamanho + 1
            return True

        atual = self.cabeca # procura a posição correta no meio ou no fim da lista
        
        while atual.proximo is not None and atual.proximo.figurinha.id < nova_figurinha.id: # laço pra quando chega no último nó ou quando acha alguém com id maior
            atual = atual.proximo

        if atual.figurinha.id == nova_figurinha.id or (atual.proximo is not None and atual.proximo.figurinha.id == nova_figurinha.id): # se ID já existir, não adiciona (vai para as repetidas)
            return False # retorna false pra avisar sistema que é repetida 

        novo_nodo.proximo = atual.proximo # encaixa novo nó ajustando setas (ponteiros)
        atual.proximo = novo_nodo
        self.tamanho = self.tamanho + 1
        return True
    
    def remover(self, id_fig):
        if self.cabeca is None: # se estiver vazio, não há o que remover
            return False

        if self.cabeca.figurinha.id == id_fig: # figurinha que quer remover é logo a primeira (cabeça)
            self.cabeca = self.cabeca.proximo # cabeça passa a ser o segundo nó
            self.tamanho = self.tamanho - 1
            return True

        atual = self.cabeca # procurar figurinha no resto da lista
        
        while atual.proximo is not None and atual.proximo.figurinha.id != id_fig: # laço anda até final da lista ou até achar nó anterior que quer remover
            atual = atual.proximo

        if atual.proximo is not None: # se saiu do laço e encontra o nó correto
            nodo_remover = atual.proximo
            atual.proximo = nodo_remover.proximo # anterior pula nó removido e aponta para seguinte
            self.tamanho = self.tamanho - 1
            return True

        return False # figurinha não encontrada
    
    def buscar_por_id(self, id_fig):
        atual = self.cabeca

        while atual is not None: # enquanto não chegar ao fim da lista
            if atual.figurinha.id == id_fig:
                return atual.figurinha # retorna objeto figurinha se encontrar
            atual = atual.proximo # anda pro próximo nó

        return None # retorna none se não achar
    
    def buscar_por_jogador(self, nome_jogador):
        atual = self.cabeca

        while atual is not None:
            if atual.figurinha.nome == nome_jogador:
                return atual.figurinha  # encontrou jogador
            atual = atual.proximo

        return None  # não encontrou

    def buscar_por_selecao(self, nome_pais): # como podem existir várias figurinhas do mesmo país, 
        atual = self.cabeca                  # exibe na tela todas as que forem encontradas
        encontrou = False

        while atual is not None:
            if atual.figurinha.pais == nome_pais:
                print(atual.figurinha)
                encontrou = True
            atual = atual.proximo

        if encontrou == False:
            print(f'Nenhuma figurinha da seleção {nome_pais} foi encontrada.')

    def calcular_porcentagem(self, total_album):
        if total_album == 0: # se álbum total tiver, por exemplo, 100 figurinhas no total
            return 0.0
        
        porcentagem = (self.tamanho / total_album) * 100
        return porcentagem
    
    def pacotinho_inserir_figurinha(self, nova_figurinha, album_repetidas):
        conseguiu_inserir = self.adicionar(nova_figurinha) # tenta colocar no próprio álbum (self)
        
        if conseguiu_inserir == False: # se retornar false, significa que id já existe (repetida)
            album_repetidas.adicionar(nova_figurinha)
            print(f'Figurinha {nova_figurinha.nome} é REPETIDA! Foi para as repetidas.')
            return False
        else:
            print(f'Figurinha {nova_figurinha.nome} é NOVA! Foi colada no álbum.')
            return True