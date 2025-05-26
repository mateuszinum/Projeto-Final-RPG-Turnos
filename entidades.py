import random
from rich.theme import Theme
from rich.console import Console
from animacoes import *

custom_theme = Theme({
    "default": "bold grey82"
})

console = Console(theme=custom_theme)


# Ações das Entidades


class Personagem:
    def __init__(self, nome, vida, ataque, defesa, velocidade, level, arma_inicial, qnt_pocoes):
        self.nome = nome
        self.vida_max = vida
        self.vida_atual = vida
        self.ataque = ataque
        self.defesa_inicial = defesa
        self.defesa_atual = defesa
        self.velocidade = velocidade
        self.xp_atual = 0
        self.xp_max = 100 * (level ** 1.5)
        self.level = level
        self.inventario = [arma_inicial]
        self.arma = arma_inicial
        self.pocoes = qnt_pocoes
    
    def ataca(self):
        acertou = random.choices([True, False], weights=[90, 10])[0]
        if acertou:
            bonus_critico = int(self.ataque * 0.3)

            chance_critico_total = min(100, self.arma.critico + bonus_critico)

            critico = random.choices([True, False], weights=[chance_critico_total, 100 - chance_critico_total])[0]
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
            return random.choices([True, False], weights=[65 + self.velocidade * 0.5, 35 - self.velocidade * 0.5])[0]
            
        else:
            return random.choices([True, False], weights=[90, 10])[0]

    def contra_atacar(self):
        if self.velocidade * 0.3 <= 60:
            return random.choices([True, False], weights=[30 + self.velocidade * 0.3, 70 - self.velocidade * 0.3])

        else:
            return random.choices([True, False], weights=[90, 10])[0]
    
    def usar_pocao(self):
        if self.pocoes > 0:
            if (self.vida_atual + self.vida_max * 0.3) > self.vida_max:
                self.vida_atual = self.vida_max

            else:
                self.vida_atual += self.vida_max * 0.3
            self.pocoes -= 1
            return True
        
        else:
            return False

    def defender_se(self):
        self.defesa_atual += self.defesa_atual * 0.5
        return True


    def receber_dano(self, dano):
        redução = self.defesa_atual * 0.5
        dano_final = max(0, dano * (1 - redução/100))
        self.vida_atual -= dano_final

    def receber_xp(self, xp):
        pontos = 0
        upou = False
        while (xp + self.xp_atual) > self.xp_max:
            xp = xp - (self.xp_max - self.xp_atual)
            self.level += 1
            upou = True
            pontos += 5
            self.xp_atual = 0
            self.xp_max = 100 * (self.level ** 1.5)
        
        return upou, pontos
    
    def upar_personagem(self):
        atributos = ['Vida', 'Ataque', 'Defesa', 'Velocidade']
        # Pedir pra o usuario escolher um desses atributos para upar
        if 'Vida':
            self.vida_max += 50
            console.print("Você upou Vida!")
            console.print("Vida antiga >> Vida nova")
        elif 'Ataque':
            self.ataque += 10
            console.print("Você upou Ataque!")
            console.print("Ataque antigo >> Ataque novo")
        elif 'Defesa':
            self.defesa += 5
            console.print("Você upou Defesa!")
            console.print("Defesa antiga >> Defesa nova")
        elif 'Velocidade':
            self.velocidade += 10
            console.print("Você upou Velocidade!")
            console.print("Velocidade antiga >> Velocidade nova")

    def verificar_personagem(self):
        # Printar cada atributo do personagem bunitin
        pass
    
class Arma: 
    def __init__(self, dano, critico):
        self.dano = dano
        self.critico = critico



class Inimigo:
    def __init__(self, nome, raca, vida, ataque, defesa, velocidade, arma_inicial):
        self.nome = nome
        self.raca = raca
        self.vida_max = vida
        self.vida_atual = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.xp_atual = 0
        self.inventario = [arma_inicial]
        self.arma = arma_inicial

class Jogo:
    def __init__(self, personagem, inimigo):
        self.personagem = personagem
        self.inimigo = inimigo
        self.acao_jogador = {
            'atacar': 1,
            'esquivar': 2,
            'contra_atacar': 3,
            'tomar_pocao': 4,
            'defender': 5
        }
    def executar(self):
        primeira_acao = True
        while True:
            if self.personagem.velocidade >= self.inimigo.velocidade:
                resultado = self.executar_acao_personagem()

                if self.verificar_fim():
                    break
                
                self.acao_inimigo(resultado)

                if self.verificar_fim():         
                    break
                
                if resultado['acao'] == 5:
                    self.personagem.defesa_atual = self.personagem.defesa_inicial
                
            else:
                if primeira_acao:
                    resultado = {
                        "acao": 1,
                        "sucesso": False,
                        "critico": False,
                        "dano": 0   
                    }

                self.acao_inimigo(resultado)

                if self.verificar_fim():
                    break
                
                if resultado['acao'] == 5:
                    self.personagem.defesa_atual = self.personagem.defesa_inicial
                
                resultado = self.executar_acao_personagem()

                primeira_acao = False

                if self.verificar_fim():
                    break

        self.personagem.vida_atual = self.personagem.vida_max

    def verificar_fim(self):
        if self.inimigo.vida_atual <= 0:
            console.print("inimigo derrotado")
            
            upou, pontos = self.personagem.receber_xp((self.inimigo.level ** 1.3) * 150)

            if upou:
                #Mensagem falando que o personagem upou
                for i in range(0, pontos):
                    self.personagem.upar_personagem()

            return True
        
        elif self.personagem.vida_atual <= 0:
            console.print("você morreu")

            return True
        
        return False
    
    def executar_acao_personagem(self):
        acao = self.obter_acao_personagem()
        resultado = self.acao_personagem(acao)

        if resultado['acao'] == self.acao_jogador['atacar']:
            ataque_personagem(self.inimigo)
            if resultado["sucesso"]:
                msg = "Você acertou o ataque"

                if resultado["critico"]:
                    msg += " CRÍTICO"

                msg += f", causando {resultado['dano']} de dano."
                monstro_atingido(self.inimigo)
            else:
                msg = "Você errou o ataque."

            
            console.print(msg)
        
        elif resultado['acao'] == self.acao_jogador['tomar_pocao']:
            console.print("você tomou a poção com sucesso")

        return resultado
            
    def acao_inimigo(self, resultado):
        dano, critou = self.inimigo.ataca()
        if dano != 0:
            ataque_monstro(self.inimigo)
            if resultado['acao'] == self.acao_jogador['esquivar']:
                if resultado['sucesso']:
                    console.print("inimigo atacou, sucesso na esquiva")

                else:
                    if critou:
                        console.print("inimigo atacou com crítico, falha na esquiva")
                    
                    else:
                        console.print("inimigo atacou, falha na esquiva")
                    personagem_atingido(self.inimigo)
                    self.personagem.vida_atual -= dano

            elif resultado['acao'] == self.acao_jogador['contra_atacar']:
                if resultado['sucesso']:
                    console.print("inimigo atacou, sucesso no contra ataque")
                    monstro_atingido(self.inimigo)
                    self.inimigo.vida_atual -= self.personagem.ataque + self.personagem.arma.dano
                
                else:
                    console.print("inimigo atacou, falha no contra ataque")
                    personagem_atingido(self.inimigo)
            else:
                chance_bloqueio = min(40, self.personagem.defesa_atual * 0.2)

                bloqueou = random.choices([True, False], weights=[chance_bloqueio, 100 - chance_bloqueio])[0]

                if not bloqueou:
                    if critou:
                        console.print("inimigo atacou com crítico")

                    else:
                        console.print("inimigo atacou")
                    personagem_atingido(self.inimigo)
                    self.personagem.vida_atual -= dano
                else:
                    console.print("o ataque do inimigo foi bloqueado")

    def acao_personagem(self, acao):
        while True:
            resultado = {
                "acao": acao,
                "sucesso": False,
                "critico": False,
                "dano": 0
            }

            if acao == 1:  
                dano, critou = self.personagem.ataca()
                if dano > 0:
                    self.inimigo.vida_atual -= dano
                    resultado["sucesso"] = True
                    resultado["dano"] = dano
                    resultado["critico"] = critou
                return resultado

            elif acao == 2:  
                resultado["sucesso"] = self.personagem.esquivar()
                return resultado

            elif acao == 3:  # 
                resultado["sucesso"] = self.personagem.contra_atacar()
                return resultado

            elif acao == 4:  
                sucesso = self.personagem.usar_pocao()

                if sucesso:
                    resultado["sucesso"] = True
                    return resultado
                
                else:
                    console.print("você não possui nenhuma poção")
                    acao = self.obter_acao_personagem()
                    continue
            
            elif acao == 5:
                resultado['sucesso'] = self.personagem.defender_se()
                return resultado

    def obter_acao_personagem(self):
        acoes = (
            "\n(1) - Atacar"
            "(2) - Esquivar"
            "(3) - Contra Atacar"
            "(4) - Tomar poção\n"
        )
        try:
            while True:
                console.print(acoes)
                escolha = int(console.input("[bold grey82]Escolha a ação: "))
                if escolha < 1 and escolha > 4:
                    raise ValueError
                return escolha
        except ValueError:
            console.print("[bold red]Escolha uma ação válida!")


# CLASSES


# Função: Absorve dano, ideal para segurar o inimigo por muito tempo.
tanque = Personagem(
    nome="Tanque",
    vida=350,
    ataque=20,
    defesa=50,
    velocidade=10,
    level=1,
    arma_inicial=Arma(dano=10, critico=5),
    qnt_pocoes=3
)

# Função: Equilíbrio entre ataque e defesa.
cavaleiro = Personagem(
    nome="Cavaleiro",
    vida=250,
    ataque=30,
    defesa=30,
    velocidade=20,
    level=1,
    arma_inicial=Arma(dano=15, critico=10),
    qnt_pocoes=3
)

# Função: Alta chance de crítico, esquiva e contra-ataque.   ######## Assassino não tá mt broken com essa arma aí? por mim diminui o dano da arma e a velocidade em 10
assassino = Personagem(
    nome="Assassino",
    vida=150,
    ataque=40,
    defesa=10,
    velocidade=40,
    level=1,
    arma_inicial=Arma(dano=25, critico=25),
    qnt_pocoes=2
)

mago = Inimigo(
    nome="Mago",
    raca="Mago",
    vida=100,
    ataque=15,
    defesa=10,
    velocidade=25,
    arma_inicial=Arma(dano=15, critico=15)
)