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
    
    def ataca(self):
        acertou = random.choices([True, False], weights=[90, 10])[0]
        if acertou:
            critico = random.choices([True, False], weights=[self.arma.critico, 100 - self.arma.critico])
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

    def executar(self):
        while True:
            if self.personagem.velocidade >= self.inimigo.velocidade:
                acao_esquiva, esquivou, acao_contra_ataca, contra_atacou = self.acao_personagem(self.personagem, self.inimigo)

                if self.inimigo.vida_atual <= 0:
                    print()#Mensagem falando que o inimigo foi derrotado

                    break

                self.acao_inimigo(self.inimigo, self.personagem, acao_esquiva, esquivou, acao_contra_ataca, contra_atacou)

                if self.inimigo.vida_atual <= 0:
                    print()#Mensagem falando que o inimigo foi derrotado

                    upou, pontos = self.personagem.receber_xp((self.inimigo.level ** 1.3) * 150)

                    if upou:
                        #Mensagem falando que o personagem upou
                        for i in range(0, pontos):
                            personagem.upar_personagem()
                            
                    break

                elif self.personagem.vida_atual <= 0:
                    print()#Mensagem falando que o personagem foi derrotado

                    break

            else:
                acao_esquiva = esquivou = acao_contra_ataca = contra_atacou = False

                self.acao_inimigo(self.inimigo, self.personagem, acao_esquiva, esquivou, acao_contra_ataca, contra_atacou)

                if self.inimigo.vida_atual <= 0:
                    print()#Mensagem falando que o inimigo foi derrotado

                    upou, pontos = self.personagem.receber_xp((self.inimigo.level ** 1.3) * 150)

                    if upou:
                        #Mensagem falando que o personagem upou
                        for i in range(0, pontos):
                            self.personagem.upar_personagem()
                            
                    break

                elif self.personagem.vida_atual <= 0:
                    print()#Mensagem falando que o personagem foi derrotado

                    break
                
                acao_esquiva, esquivou, acao_contra_ataca, contra_atacou = self.acao_personagem(self.personagem, self.inimigo)

                if self.inimigo.vida_atual <= 0:
                    print()#Mensagem falando que o inimigo foi derrotado
                    
                    upou, pontos = self.personagem.receber_xp((self.inimigo.level ** 1.3) * 150)

                    if upou:
                        #Mensagem falando que o personagem upou
                        for i in range(0, pontos):
                            self.personagem.upar_personagem()

                    break

    def acao_inimigo(inimigo, personagem, acao_esquiva, esquivou, acao_contra_ataca, contra_atacou):
        dano, critou = inimigo.ataca()
        if dano != 0:
            if acao_esquiva:
                if esquivou:
                    print()#Mensagem dizendo que o inimigo atacou mas o personagem conseguiu esquivar

                else:
                    if critou:
                        print()#Mensagem dizendo que o inimigo atacou e critou e o personagem nao conseguiu esquivar
                    else:
                        print()#Mensagem dizendo que o inimigo atacou e o personagem nao conseguiu esquivar

                    personagem.vida_atual -= dano

            elif acao_contra_ataca:
                if contra_atacou:
                    print()#Mensagem dizendo que o inimigo atacou mas o personagem conseguiu contra atacar

                    inimigo.vida_atual -= personagem.ataque + personagem.arma.dano
                
                else:
                    print()#Mensagem dizendo que o inimigo atacou e o personagem falhou em contra atacar
            else:
                if critou:
                    print()#Mensagem dizendo que o inimigo atacou e critou

                else:
                    print()#Mensagem dizendo que o inimigo atacou

                personagem.vida_atual -= dano



    def acao_personagem(personagem, inimigo):
        # Mensagem perguntando qual ação ele quer executar
        if 'Ataca':
            dano, critou = personagem.ataca()

            if dano != 0:
                if critou:
                    print()#Mensagem falando que o ataque deu certo e que critou

                else:
                    print()#Mensagem falando que o ataque deu certo

                inimigo.vida_atual -= dano

            else:
                print()#Mensagem falando que o ataque falhou

            return False, False, False, False
            #Tudo False, pq ele nao esquivou nem contra atacou


        elif 'Esquiva':
            return True, personagem.esquivar(), False, False
            # True pq ele esquivou, função q vai retornar se deu certo a esquiva, false pq n contra atacou, false pq n contra atacou

        
        elif 'Contra Atacar':
            return False, False, True, personagem.contra_atacar()
            # False pq ele nao esquivou, False pq ele n esquivou, True pq ele contra atacou, função q vai retornar se deu certo o contra ataque

        #Todos esses return de false e true, servem para personalizar as mensagens que vai ser mandada, pra caso esquivou e falhou, ou esquivou e deu certo etc etc, uma mensagem pra cada situação

        elif 'Tomar poção':
            personagem.usar_pocao()

# Testes
xp = "==========================================60%======----------------------------"
texto_vazio = "\n\n\n\n\n\n\n\n\n"
colunas = Columns([animacoes.ogro, texto_vazio + animacoes.esqueleto], padding=(0, 30))
console.print(Panel(colunas, title=f"[bold green] {xp}", border_style="purple"))