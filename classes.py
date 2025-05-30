import time
import random
from sql import *
import animacoes as cena
from rich.panel import Panel
from rich.theme import Theme
from rich.columns import Columns
from rich.console import Console


tema = Theme({
    "default": "bold grey82"
})


console = Console(theme=tema)


# Ações das Entidades


class Personagem:
    def __init__(self, nome, vida, ataque, defesa, velocidade, level, arma, qnt_pocoes, chave):
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
        self.arma = arma
        self.pocoes_max = qnt_pocoes
        self.pocoes_atual = qnt_pocoes
        self.chave = chave

        if not personagem_existe(self.nome):
            self.id = insert_personagem_e_retorna_id(self)

        else:
            cursor.execute("SELECT ID FROM Personagens WHERE Nome = ?", (self.nome,))
            self.id = cursor.fetchone()[0]
            
            dados = carregar_dados_personagem_completo(self.nome)

            self.vida_max, self.ataque, self.defesa_inicial, self.velocidade, self.pocoes_max, self.level, self.xp_atual, chave = dados
            self.vida_atual = self.vida_max
            self.defesa_atual = self.defesa_inicial
            self.pocoes_atual = self.pocoes_max
            self.xp_max = 100 * (self.level ** 1.5)
            self.chave = chave


    def ataca(self):
        acertou = random.choices([True, False], weights=[90, 10])[0]
        if acertou:
            bonus_critico = int(self.ataque * 0.3)

            chance_critico_total = min(100, self.arma.critico + bonus_critico)

            critico = random.choices([True, False], weights=[chance_critico_total, 100 - chance_critico_total])[0]
            if critico:
                return (self.ataque + self.arma.dano) * 2, critico

            else:
                return self.ataque + self.arma.dano, critico

        else:
            return 0, False

            
    def esquivar(self):
        if self.velocidade * 0.5 <= 25:
            return random.choices([True, False], weights=[65 + self.velocidade * 0.5, 35 - self.velocidade * 0.5])[0]
            
        else:
            return random.choices([True, False], weights=[90, 10])[0]

    def contra_atacar(self):
        if self.velocidade * 0.2 <= 70:
            return random.choices([True, False], weights=[20 + self.velocidade * 0.2, 80 - self.velocidade * 0.2])[0]
        
        else:
            return random.choices([True, False], weights=[90, 10])[0]
    
    def usar_pocao(self):
        if self.pocoes_atual > 0:
            if (self.vida_atual + self.vida_max * 0.3) > self.vida_max:
                self.vida_atual = self.vida_max

            else:
                self.vida_atual += int(self.vida_max * 0.3)
            self.pocoes_atual -= 1
            return True
        
        else:
            return False

    def defender_se(self):
        self.defesa_atual += self.defesa_atual * 0.5
        return True


    def receber_dano(self, dano):
        redução = min(90, self.defesa_atual * 0.5)
        dano_final = dano * (1 - redução/100)
        self.vida_atual -= int(dano_final)
        return int(dano_final)

    def receber_xp(self, xp):
        pontos = 0
        upou = False
        while (xp + self.xp_atual) > self.xp_max:
            xp = xp - (self.xp_max - self.xp_atual)
            self.level += 1
            upou = True
            pontos += 3
            self.xp_atual = 0
            self.xp_max = 100 * (self.level ** 1.5)
        
        return upou, pontos
    
    def upar_personagem(self, pontos):
        console.clear()

        atributos = ['[bold bright_green]Vida', 
                    '[bold red1]Ataque', 
                    '[bold bright_yellow]Defesa', 
                    '[bold dodger_blue2]Velocidade']
        
        console.print(f"\n\n\n{' ' * 20}Pontos restantes: [bold plum1]{3 - pontos}\n", style="default")
        for i, atributo in enumerate(atributos, 1):
            console.print(f"{' ' * 20}([bold plum1]{i}[/]) - {atributo}", style="default")
        
        escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha um atributo para upar: ")

        if escolha == '1':
            self.vida_max += 50
            console.print(f"\n\n\n{' ' * 20}Você upou [bold bright_green]Vida[/]!", style="default")
            console.print(f"{' ' * 20}[bold bright_green]{self.vida_max - 50} >> [bold bright_green]{self.vida_max}", style="default")

        elif escolha == '2':
            self.ataque += 10
            console.print(f"\n\n\n{' ' * 20}Você upou [bold red1]Ataque[/]!", style="default")
            console.print(f"{' ' * 20}[bold red1]{self.ataque - 10} >> [bold red1]{self.ataque}", style="default")

        elif escolha == '3':
            self.defesa_inicial += 5
            self.defesa_atual = self.defesa_inicial
            console.print(f"\n\n\n{' ' * 20}Você upou [bold bright_yellow]Defesa[/]!", style="default")
            console.print(f"{' ' * 20}[bold bright_yellow]{self.defesa_inicial - 5} >> [bold bright_yellow]{self.defesa_inicial}", style="default")
        
        elif escolha == '4':
            self.velocidade += 10
            console.print(f"\n\n\n{' ' * 20}Você upou [bold dodger_blue2]Velocidade[/]!", style="default")
            console.print(f"{' ' * 20}[bold dodger_blue2]{self.velocidade - 10} >> [bold dodger_blue2]{self.velocidade}", style="default")
        
        else:
            console.print(f"\n{' ' * 20}[bold red1]Escolha inválida! Tente novamente.")
            time.sleep(1)
            self.upar_personagem(pontos)

        time.sleep(1)

    def verificar_personagem(self):
        console.clear()
        heroi = cena.criar_personagem_ascii()
        mensagem = (
            f"\n\n\n[bold bright_green]Vida: {self.vida_max}[/]  | [bold red1]Ataque: {self.ataque}[/]\n"
            f"[bold bright_yellow]Defesa: {self.defesa_inicial}[/] | [bold dodger_blue2]Velocidade: {self.velocidade}[/]\n"
            f"Inventário:\n"
            f"\n{' ' * 2}- [bold]Arma: [bold red1]{self.arma.dano} DMG[/] ([bold orange1]Crítico: {self.arma.critico}%[/])\n"
            f"{' ' * 2}- [bold]Poções: [bold green_yellow]{self.pocoes_atual}\n"
        )
        if self.chave:
            mensagem += f"{' ' * 2}- [bold light_goldenrod1]Chave do Boss\n"

        colunas = Columns([heroi, mensagem], equal=True, expand=True) 
        console.print(Panel.fit(colunas, title=f"[bold grey82]{self.nome} - Nível [bold plum1]{self.level}[/]", border_style="medium_orchid", style="default", width=90))
        pass
    


class Arma: 
    def __init__(self, nome, dano, critico):
        self.nome = nome
        self.dano = dano
        self.critico = critico



class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa, velocidade, level, arma, qnt_pocoes, chave, raca, tipo):
        super().__init__(nome, vida, ataque, defesa, velocidade, level, arma, qnt_pocoes, chave)
        self.raca = raca
        self.tipo = random.choices(tipo, weights=[50, 50])[0]
        self.id = insert_inimigo_e_retorna_id(self)



class Jogo:
    def __init__(self, heroi, inimigo):
        self.heroi = heroi
        self.inimigo = inimigo
        self.acao_jogador = {
            'atacar': 1,
            'esquivar': 2,
            'contra_atacar': 3,
            'tomar_pocao': 4,
            'defender': 5
        }
        self.id = insert_jogo_e_retorna_id(heroi.id, inimigo.id)
        
    def executar(self):
        primeira_acao = True
        acabou = False
        while True and self.heroi.velocidade >= self.inimigo.velocidade and not acabou:
            resultado = self.executar_acao_personagem()
            
            turno_id = insert_turno_e_retorna_id(self.heroi.id, self.inimigo.id, resultado['acao'], "Heroi", resultado["sucesso"])
            insert_historico(self.id, turno_id, self.heroi.vida_atual, self.inimigo.vida_atual)

            if self.verificar_fim():
                acabou = True
                break
            
            sucesso = self.acao_inimigo(resultado)

            turno_id = insert_turno_e_retorna_id(self.heroi.id, self.inimigo.id, 1, "inimigo", sucesso)
            insert_historico(self.id, turno_id, self.heroi.vida_atual, self.inimigo.vida_atual)

            if self.verificar_fim():  
                acabou = True       
                break
            
            if resultado['acao'] == 5:
                self.heroi.defesa_atual = self.heroi.defesa_inicial
        
        while True and self.heroi.velocidade < self.inimigo.velocidade and not acabou:
            if primeira_acao:
                resultado = {
                    "acao": 1,
                    "sucesso": False,
                    "critico": False,
                    "dano": 0   
                }

            sucesso = self.acao_inimigo(resultado)

            time.sleep(3)

            turno_id = insert_turno_e_retorna_id(self.heroi.id, self.inimigo.id, 1, "Inimigo", sucesso)

            if self.verificar_fim():
                acabou = True
                break

            if resultado['acao'] == 5:
                self.heroi.defesa_atual = self.heroi.defesa_inicial
            
            resultado = self.executar_acao_personagem()
            
            insert_turno_e_retorna_id(self.heroi.id, self.inimigo.id, resultado["acao"])

            primeira_acao = False

            if self.verificar_fim():
                acabou = True
                break

        self.heroi.vida_atual = self.heroi.vida_max
        self.heroi.pocoes_atual = self.heroi.pocoes_max


    def verificar_fim(self):
        if self.inimigo.vida_atual <= 0:
            cena.criar_cena(self.heroi, self.inimigo)
            console.print(f"\n\n\n{' ' * 20}[bold light_goldenrod1]Inimigo derrotado!", style="default")
            console.print(f"{' ' * 20}[bold plum1]+{int((self.inimigo.level ** 1.3) * 150)} XP", style="default")
            time.sleep(3)

            upou, pontos = self.heroi.receber_xp(275 * self.inimigo.level**2 - 550 * self.inimigo.level + 425)

            if upou:
                console.print(f"\n\n\n{' ' * 20}[bold green_yellow]Você subiu de nível![/] Você atingiu o nível [bold plum1]{self.heroi.level}[/]!", style="default")
                time.sleep(3)
                for i in range(0, pontos):
                    self.heroi.upar_personagem(i)

            if self.inimigo.chave and not self.heroi.chave:
                console.print(f"\n\n\n{' ' * 20}Você encontrou: [bold green_yellow]Chave do Boss[/]!", style="default")
                self.heroi.chave = True

            atualiza_heroi(self.heroi.id, self.heroi.vida_max, self.heroi.ataque, self.heroi.defesa_inicial, self.heroi.velocidade, self.heroi.level, self.heroi.xp_atual, self.heroi.pocoes_max, self.heroi.chave)           
            
            atualiza_vencedor_jogo(self.id, self.heroi.id)

            return True
        
        elif self.heroi.vida_atual <= 0:
            cena.criar_cena(self.heroi, self.inimigo)
            console.print(f"\n\n\n{' ' * 20}[bold red3]Você foi derrotado!")
            time.sleep(1)
            console.print(f"{' ' * 20}[bold light_goldenrod1]Porém a sua aventura ainda não acabou.")
            time.sleep(3)
            console.clear()

            atualiza_vencedor_jogo(self.id, self.heroi.id)

            return True
        
        return False
    
    def executar_acao_personagem(self):
        acao = self.obter_acao_personagem()
        resultado = self.acao_personagem(acao)

        if resultado['acao'] == self.acao_jogador['atacar']:
            
            cena.avanco_personagem(self.heroi, self.inimigo)
            if resultado["sucesso"]:
                msg = "Você [bold bright_green]acertou[/] o ataque"

                if resultado["critico"]:
                    msg += "[bold orange1] crítico[/]"

                msg += f", causando [bold red1]{resultado['dano']}[/] de dano"
                
                cena.monstro_atingido(self.heroi, self.inimigo)
                self.inimigo.vida_atual -= resultado["dano"]

            else:
                msg = "Você [bold red1]errou[/] o ataque"

            cena.criar_cena(self.heroi, self.inimigo)
            console.print(f"\n\n\n{' ' * 20}{msg}", style="default")
            time.sleep(3)

        elif resultado['acao'] == self.acao_jogador['tomar_pocao']:
            cena.tomarPocao_personagem(self.heroi, self.inimigo)
            cena.criar_cena(self.heroi, self.inimigo)
            console.print(f"\n\n\n{' ' * 20}[bold green_yellow]Você tomou uma poção! [bold bright_green]+ {self.heroi.vida_max * 0.3} HP[/]")
            time.sleep(3)
        
        return resultado
            
    def acao_inimigo(self, resultado):
        dano, critou = self.inimigo.ataca()
        if dano != 0:
            cena.ataque_monstro(self.heroi, self.inimigo)
            if resultado['acao'] == self.acao_jogador['esquivar']:
                if resultado['sucesso']:
                    cena.esquiva_personagem(self.heroi, self.inimigo)
                    cena.criar_cena(self.heroi, self.inimigo)
                    console.print(f"\n\n\n{' ' * 20}Inimigo atacou, [bold bright_green]sucesso[/] na [bold dodger_blue2]esquiva[/]", style="default")
                    time.sleep(3)
                    return False
                
                else:
                    cena.personagem_atingido(self.heroi, self.inimigo)
                    dano_final = self.heroi.receber_dano(dano)
                    cena.criar_cena(self.heroi, self.inimigo)

                    if critou:
                        console.print(f"\n\n\n{' ' * 20}Inimigo atacou com [bold orange1]crítico[/], causando [bold red1]{dano_final}[/] de dano, [bold red1]falha[/] na [bold dodger_blue2]esquiva[/]", style="default")
                    
                    else:
                        console.print(f"\n\n\n{' ' * 20}Inimigo atacou, causando [bold red1]{dano_final}[/] de dano, [bold red1]falha[/] na [bold dodger_blue2]esquiva", style="default")
                    time.sleep(3)
                    return True

            elif resultado['acao'] == self.acao_jogador['contra_atacar']:
                if resultado['sucesso']:
                    cena.contraAtaque_personagem(self.heroi, self.inimigo)
                    cena.monstro_atingido(self.heroi, self.inimigo)
                    self.inimigo.vida_atual -= self.heroi.ataque + self.heroi.arma.dano
                    cena.criar_cena(self.heroi, self.inimigo)
                    console.print(f"\n\n\n{' ' * 20}Inimigo atacou, [bold bright_green]sucesso[/] no [bold bright_yellow]contra ataque[/], causou [bold red1]{self.heroi.ataque + self.heroi.arma.dano}[/] de dano", style="default")
                    time.sleep(3)
                    return False

                else:
                    
                    cena.personagem_atingido(self.heroi, self.inimigo)
                    dano_final = self.heroi.receber_dano(dano)
                    cena.criar_cena(self.heroi, self.inimigo)
                    console.print(f"\n\n\n{' ' * 20}Inimigo atacou, causando [bold red1]{dano_final}[/] de dano, [bold red1]falha[/] no [bold bright_yellow]contra ataque", style="default")
                    time.sleep(3)
                    return True

            else:
                chance_bloqueio = min(90, self.heroi.defesa_atual * 0.2)
                bloqueou = random.choices([True, False], weights=[chance_bloqueio, 100 - chance_bloqueio])[0]

                if not bloqueou:
                    
                    cena.personagem_atingido(self.heroi, self.inimigo)
                    dano_final = self.heroi.receber_dano(dano)
                    cena.criar_cena(self.heroi, self.inimigo)
                    if critou:
                        console.print(f"\n\n\n{' ' * 20}Inimigo atacou com [bold orange1]crítico[/], causando [bold red1]{dano_final}[/] de dano", style="default")

                    else:
                        console.print(f"\n\n\n{' ' * 20}Inimigo atacou, causando [bold red1]{dano_final}[/] de dano", style="default")

                    time.sleep(3)
                    return True

                else:
                    cena.bloqueio_personagem(self.heroi, self.inimigo)
                    cena.criar_cena(self.heroi, self.inimigo)
                    console.print(f"\n\n\n{' ' * 20}O ataque do inimigo foi bloqueado com [bold bright_green]sucesso[/]!", style="default")

                    time.sleep(3)
                    return False

        else:
            cena.criar_cena(self.heroi, self.inimigo)
            console.print(f"\n\n\n{' ' * 20}Inimigo [bold red1]errou[/] o ataque", style="default")
            time.sleep(3)
            return False 

    def acao_personagem(self, acao):
        while True:
            resultado = {
                "acao": acao,
                "sucesso": False,
                "critico": False,
                "dano": 0
            }

            if acao == 1:  
                dano, critou = self.heroi.ataca()
                if dano > 0:
                    resultado["sucesso"] = True
                    resultado["dano"] = dano
                    resultado["critico"] = critou
                return resultado

            elif acao == 2:  
                resultado["sucesso"] = self.heroi.esquivar()
                return resultado

            elif acao == 3:
                resultado["sucesso"] = self.heroi.contra_atacar()
                return resultado

            elif acao == 4:  
                sucesso = self.heroi.usar_pocao()

                if sucesso:
                    resultado["sucesso"] = True
                    return resultado
                
                else:
                    console.print(f"\n\n\n{' ' * 20}[bold red1]Você não possui nenhuma poção")
                    time.sleep(3)
                    acao = self.obter_acao_personagem()
                    continue
            
            elif acao == 5:
                resultado['sucesso'] = self.heroi.defender_se()
                return resultado
            
            else:
                console.print(f"\n\n\n{' ' * 20}[bold red1]Ação inválida. Escolha novamente.")
                time.sleep(3)
                acao = self.obter_acao_personagem()

    def obter_acao_personagem(self):

        cena.criar_cena(self.heroi, self.inimigo)

        console.print(f"\n\n\n")

        acoes = (
            f"\n\n\n{' ' * 20}([bold plum1]1[/]) - Atacar"
            f"\n{' ' * 20}([bold plum1]2[/]) - Esquivar"
            f"\n{' ' * 20}([bold plum1]3[/]) - Contra Atacar"
            f"\n{' ' * 20}([bold plum1]4[/]) - Tomar poção"
            f"\n{' ' * 20}([bold plum1]5[/]) - Defender"
        )
        try:
            while True:
                console.print(f"{acoes}", style="default")
                escolha = int(console.input(f"\n{' ' * 20}[bold grey82]Escolha a ação: "))
                if escolha < 1 and escolha > 5:
                    raise ValueError
                return escolha
        except ValueError:
            console.print(f"\n{' ' * 20}[bold red1]Escolha uma ação válida!")