import animacoes
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns


console = Console()


class Personagem:
    def __init__(self, nome, vida, ataque, defesa, experiencia):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.experiencia = experiencia
        self.inventario = [] # começar com algum item já
    
    def atacar(self):
        pass

    def esquivar(self):
        pass

    def curar(self):
        pass

class Inimigo(Personagem):
    def __init__(self, raca):
        self.raca = raca    

class Jogo:
    pass

class Arma: # ?
    pass


# Testes
xp = "==========================================60%======----------------------------"
texto_vazio = "\n\n\n\n\n\n\n\n\n"
colunas = Columns([animacoes.ogro, texto_vazio + animacoes.esqueleto], padding=(0, 30))
console.print(Panel(colunas, title=f"[bold green] {xp}", border_style="purple"))