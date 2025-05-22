import animacoes
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
import random

console = Console()


class Personagem:
    def __init__(self, nome, vida, ataque, defesa, velocidade ,level, arma_inicial, qnt_pocoes):
        self.nome = nome
        self.vida_max = vida
        self.vida_atual = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.xp_atual = 0
        self.xp_max = 100 * (level ** 1.5)
        self.level = level
        self.inventario = [arma_inicial]
        self.arma = arma_inicial
        self.pocoes = qnt_pocoes
    
    def atacar(self):
        acertou = random.choice([True, False], weights=[90, 10])[0]
        if acertou:
            critico = random.choice([True, False], weights=[self.arma.critico, 100 - self.arma.critico])
            if critico:
                return (self.ataque + self.arma.dano) * 2, critico
                # Retorna o dano, e o True, pra na msg vc poder falar que critou e mostrar o dano
            else:
                return self.ataque + self.arma.dano, critico
                # Retorna o dano, e o False, pra vc n precisar falar que critou e apenas mostrar o dano
        else:
            return 0
            # Caso o ataque de 0 de dano, vc coloca uma mensagem dizendo que o ataque falhou
            
    def esquivar(self):
        if self.velocidade * 0.5 <= 25:
            return random.choice([True, False], weights=[65 + self.velocidade * 0.5, 35 - self.velocidade * 0.5])[0]
            
        else:
            return random.choice([True, False], weights=[90, 10])[0]

    def contra_atacar(self):
        if self.velocidade * 0.3 <= 60:
            return random.choice([True, False], weights=[30 + self.velocidade * 0.3, 70 - self.velocidade * 0.3])

        else:
            return random.choice([True, False], weights=[90, 10])[0]
    
    def usar_pocao(self):
        if self.pocoes > 0:
            if (self.vida_atual + 50) > self.vida_max:
                self.vida_atual = self.vida_max

            else:
                self.vida_atual += 50
            self.pocoes -= 1
            return True
        
        else:
            return False

    def receber_dano(self, dano):
        self.vida_atual -= dano - self.defesa

    def receber_xp(self, xp):
        pontos = 0
        upou = False
        while (xp + self.xp_atual) > self.xp_max:
            xp = xp - (self.xp_max - self.xp_atual)
            level += 1
            upou = True
            pontos += 5
            self.xp_atual = 0
            self.xp_max = 100 * (level ** 1.5)
        
        return upou, pontos
    
    def upar_personagem(self):
        atributos = ['Vida', 'Ataque', 'Defesa', 'Velocidade']
        # Pedir pra o usuario escolher um desses atributos para upar
        if 'Vida':
            self.vida_max += 50
            # Mensagem falando que ele upou a vida e mostrar o novo valor de vida_max
        elif 'Ataque':
            self.ataque += 10
            # Mensagem falando que ele upou o ataque e mostrar o novo valor de ataque
        elif 'Defesa':
            self.defesa += 5
            # Mensagem falando que ele upou a defesa e mostrar o novo valor de defesa
        elif 'Velocidade':
            self.velocidade += 10
            # Mensagem falando que ele upou a velocidade e mostrar o novo valor de velocidade

    def verificar_personagem(self):
        # Printar cada atributo do personagem bunitin
        pass
    
class Arma: 
    def __init__(self, dano, critico):
        self.dano = dano
        self.critico = critico



class Inimigo(Personagem):
    def __init__(self, raca):
        self.raca = raca    

class Jogo:
    pass



# Testes
xp = "==========================================60%======----------------------------"
texto_vazio = "\n\n\n\n\n\n\n\n\n"
colunas = Columns([animacoes.ogro, texto_vazio + animacoes.esqueleto], padding=(0, 30))
console.print(Panel(colunas, title=f"[bold green] {xp}", border_style="purple"))