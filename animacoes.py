import time
from rich.text import Text
from rich.panel import Panel
from rich.console import Console


console = Console()     


CORES = {
    "monstro": "",
    "personagem": "grey46",
    "projetil": ""
}


def criar_mago():
    return Text.from_markup(
rf"""[bold {CORES["monstro"]}]
         ,    _
        /|   | |
      _/_\_  >_<
     .-\-/.   |
    /  | | \_ |
    \ \| |\__(/
    /(`---')  |
   / /     \  |
_.'  \-'-'  / |
`----'`=-='   '
[/]""")



def criar_personagem():
    return Text.from_markup(
rf"""[bold {CORES["personagem"]}]

  /\      .-.
  ||    __|=|__
   ||   (_/`-`\_)
  _||_  //\___/\\
   \/<__> /   \<>
          |_._|/
          <_I_>
           |||
          /_|_\
[/]""")


# Outros sprites do mago, não achei nenhum outro guerreiro legalzinho


# se pá dá pra arrumar esse modelo e usar como fada ou elfo mágico, sla
(rf"""[bold {CORES["monstro"]}]
       ,/   *
    _,'/_   |
    `(")' ,'/
 _ _,-H-./ /
 \_\_\.   /
  /" / \  \_
_/  /   \  \_
\_.'( ) (`._/
[/]""")


# talvez o boss?
(rf"""[bold {CORES["monstro"]}]
				 _____
	 _____	    /__ /(
	/  _  \	    `.	\ \
   |  [ () |	  \	 \ \
 .---.	  ¯|-..    \  \ \
//` \ \¯¯¯¯¯\  \  _//  \ |
\` ,' /	     ) / (,`|`--'
 `---´	 `	/-´`.// /
  |	 \	'|'( \  // /	 
  \  | _  _|  `// /
[/]""")

def vida_heroi(heroi):
    mensagem = "┃" * int(heroi.vida_atual / heroi.vida_max * 50)
    mensagem += "‒" * (50 - len(mensagem))
    
    if heroi.vida_atual <= 0:
        heroi.vida_atual = 0

    texto_vida = f" {heroi.vida_atual}/{heroi.vida_max} "
    meio = len(mensagem) // 2
    inicio = meio - len(texto_vida) // 2
    fim = inicio + len(texto_vida)
    
    barra_com_texto = (mensagem[:inicio] + texto_vida + mensagem[fim:])
    
    return barra_com_texto


def vida_monstro(inimigo):
    mensagem = "┃" * int(inimigo.vida_atual / inimigo.vida_max * 50)
    mensagem += "‒" * (50 - len(mensagem))
    
    if inimigo.vida_atual <= 0:
        inimigo.vida_atual = 0

    texto_vida = f" {inimigo.vida_atual}/{inimigo.vida_max} "
    meio = len(mensagem) // 2
    inicio = meio - len(texto_vida) // 2
    fim = inicio + len(texto_vida)
    
    barra_com_texto = (mensagem[:inicio] + texto_vida + mensagem[fim:])
    
    return barra_com_texto


def cria_monstro(inimigo):
    if inimigo.tipo == "Fogo":
        CORES["monstro"] = "hot_pink3"
        CORES["projetil"] = "orange_red1"

    elif inimigo.tipo == "Gelo":
        CORES["monstro"] = "cornflower_blue"
        CORES["projetil"] = "deep_sky_blue1"

    if inimigo.nome == "Mago":
        monstro = criar_mago()

    return monstro


# Cena estática
def criar_cena(heroi, inimigo):
    console.clear()

    monstro = cria_monstro(inimigo)
    personagem = criar_personagem()

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * 100)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))


def avanco_personagem(heroi, inimigo):
    # Ataque do Personagem
    console.clear()

    monstro = cria_monstro(inimigo)
    personagem = criar_personagem()

    for pos in [100, 80, 60, 40, 60, 80, 100]:
        
        cena = Text()
        for linha_m, linha_p in zip(monstro.split(), personagem.split()):
            cena.append(linha_m)
            cena.append(' ' * pos)
            cena.append(linha_p)
            cena.append('\n')
        
        console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))
        time.sleep(0.6)
        console.clear()


def personagem_atingido(heroi, inimigo):
    
    borda = "red1"
    CORES["personagem"] = "red1"

    muda_personagem_estado(heroi, inimigo, borda)


def esquiva_personagem(heroi, inimigo):

    borda = "dodger_blue2"
    CORES["personagem"] = "dodger_blue2"

    muda_personagem_estado(heroi, inimigo, borda)


def contaAtaque_personagem(heroi, inimigo):

    borda = "bright_yellow"
    CORES["personagem"] = "bright_yellow"

    muda_personagem_estado(heroi, inimigo, borda)


def tomarPocao_personagem(heroi, inimigo):

    borda = "bright_green"
    CORES["personagem"] = "bright_green"

    muda_personagem_estado(heroi, inimigo, borda)


def muda_personagem_estado(heroi, inimigo, borda):
    # Personagem toma dano
    console.clear()

    monstro = cria_monstro(inimigo)
    personagem = criar_personagem()

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * 100)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style=borda, width=140))
    time.sleep(1)
    CORES["personagem"] = "grey46"

    voltar_normal(heroi, inimigo)


def ataque_monstro(heroi, inimigo):
    # Ataque do Monstro
    console.clear()

    for pos in [20, 40, 60, 80]:
        
        monstro = cria_monstro(inimigo)

        personagem = criar_personagem()
        
        cena = Text()
        for i, (linha_m, linha_p) in enumerate(zip(monstro.split(), personagem.split())):
            if i == 5:
                cena.append(linha_m)
                cena.append(' ' * pos)
                cena.append(Text("▶", style=CORES["projetil"]))
                cena.append(Text("▶", style=CORES["projetil"]))
                cena.append(' ' * (99 - pos))
                cena.append(linha_p)
                cena.append('\n')
            else:
                cena.append(linha_m)
                cena.append(' ' * (pos + 1))
                cena.append(' ' * (100 - pos))
                cena.append(linha_p)
                cena.append('\n')
      
        console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))
        time.sleep(0.7)
        console.clear()


def monstro_atingido(heroi, inimigo):
    # Monstro toma dano
    console.clear()
    
    monstro = cria_monstro(inimigo)

    aux = CORES["monstro"]
    CORES["monstro"] = "red1"

    if inimigo.nome == "Mago":
        monstro = criar_mago()

    personagem = criar_personagem()

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * 100)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{aux}]{vida_monstro(inimigo)}", border_style=f"{CORES['monstro']}", width=140))
    time.sleep(1)

    CORES["monstro"] = aux
    voltar_normal(heroi, inimigo)


def voltar_normal(heroi, inimigo):
    # Volta ao normal
    console.clear()

    monstro = cria_monstro(inimigo)

    personagem = criar_personagem()

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * 100)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))
    time.sleep(0.6)
    console.clear()