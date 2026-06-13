class Figurinha:
    def __init__(self, id_fig: int, nome: str, pais: str, posicao: str, raridade: str):
        self.id = id_fig
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def __str__(self):
        if self.raridade != '': # se a figurinha tiver raridade
            return f'Número: {self.id} - {self.nome} ({self.pais}), posição: {self.posicao}, raridade: [{self.raridade}]'
        
        else: # se não tiver raridade
            return f'Número: {self.id} - {self.nome} ({self.pais}), posição: {self.posicao}'