class Figurinha:
    def __init__(self, id_fig: int, nome: str, pais: str, raridade: str):
        self.id = id_fig
        self.nome = nome
        self.pais = pais
        self.raridade = raridade

    def __str__(self):
        if self.raridade != '': # se a figurinha tiver raridade
            return f'Número: {self.id} - {self.nome} ({self.pais}), raridade: [{self.raridade}]'
        
        else: # se não tiver raridade
            return f'Número: {self.id} - {self.nome} ({self.pais})'