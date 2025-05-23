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
                
                self.acao_inimigo(self.inimigo, self.personagem, resultado)

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

                self.acao_inimigo(self.inimigo, self.personagem, resultado)

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
            print()#Mensagem falando que o inimigo foi derrotado
            
            upou, pontos = self.personagem.receber_xp((self.inimigo.level ** 1.3) * 150)

            if upou:
                #Mensagem falando que o personagem upou
                for i in range(0, pontos):
                    self.personagem.upar_personagem()

            return True
        
        elif self.personagem.vida_atual <= 0:
            print()#Mensagem falando que o personagem foi derrotado

            return True
        
        return False
    
    def executar_acao_personagem(self):
        acao = self.obter_acao_personagem()
        resultado = self.acao_personagem(acao)

        if resultado['acao'] == self.acao_jogador['atacar']:
            if resultado["sucesso"]:
                msg = "Você acertou o ataque"

                if resultado["critico"]:
                    msg += " CRÍTICO"

                msg += f", causando {resultado['dano']} de dano."

            else:
                msg = "Você errou o ataque."

            print()#Printar a msg bunitin, se vc quiser pode mudar o texto do jeito que quiser, mas tenta usar essa logica q eu usei ai
        
        elif resultado['acao'] == self.acao_jogador['tomar_pocao']:
            print()#Mensagem dizendo que tomou a pocao com sucesso

        return resultado
            
    def acao_inimigo(self, inimigo, personagem, resultado):
        dano, critou = inimigo.ataca()
        if dano != 0:
            if resultado['acao'] == self.acao_jogador['esquivar']:
                if resultado['sucesso']:
                    print()#Mensagem dizendo que o inimigo atacou mas o personagem conseguiu esquivar

                else:
                    if critou:
                        print()#Mensagem dizendo que o inimigo atacou e critou e o personagem nao conseguiu esquivar
                    
                    else:
                        print()#Mensagem dizendo que o inimigo atacou e o personagem nao conseguiu esquivar

                    personagem.vida_atual -= dano

            elif resultado['acao'] == self.acao_jogador['contra_atacar']:
                if resultado['sucesso']:
                    print()#Mensagem dizendo que o inimigo atacou mas o personagem conseguiu contra atacar

                    inimigo.vida_atual -= personagem.ataque + personagem.arma.dano
                
                else:
                    print()#Mensagem dizendo que o inimigo atacou e o personagem falhou em contra atacar
            else:
                chance_bloqueio = min(40, personagem.defesa_atual * 0.2)

                bloqueou = random.choices([True, False], weights=[chance_bloqueio, 100 - chance_bloqueio])[0]

                if not bloqueou:
                    if critou:
                        print()#Mensagem dizendo que o inimigo atacou e critou

                    else:
                        print()#Mensagem dizendo que o inimigo atacou

                    personagem.vida_atual -= dano
                else:
                    print()#Mensagem dizendo que o personagem bloqueou o ataque com sua defesa

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
                    print()#Mensagem dizendo que nao tem pocao
                    acao = self.obter_acao_personagem()
                    continue
            
            elif acao == 5:
                resultado['sucesso'] = self.personagem.defender_se()
                return resultado

    def obter_acao_personagem(self):
        print()#Mensagem perguntando oq ele quer fazer, atacar, esquivar, contra atacar ou tomar poca e depois retorna essa escolha
        # retornando da seguinte maneira
        # 1 - se ele quiser atacar / 2 - se ele quiser esquivar / 3 - se ele quiser contra atacar / 4 - tomar pocao

# Testes
xp = "==========================================60%======----------------------------"
texto_vazio = "\n\n\n\n\n\n\n\n\n"
colunas = Columns([animacoes.ogro, texto_vazio + animacoes.esqueleto], padding=(0, 30))
console.print(Panel(colunas, title=f"[bold green] {xp}", border_style="purple"))