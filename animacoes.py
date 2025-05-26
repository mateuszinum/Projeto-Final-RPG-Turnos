import time
from rich.text import Text
from rich.panel import Panel
from rich.console import Console

console = Console()     

CORES = {
    "monstro": "",
    "personagem": "aquamarine1",
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


(rf"""[bold {CORES["monstro"]}]
         /^\
    /\   "V"
   /__\   I
  //..\\  I
  \].`[/  I
  /l\/j\  (]
 /. ~~ ,\/I
 \_L__j^\/I
  \/--v\  I
  |    |  I
  |    |  I
  |    l  I
_/j  L l\_!
[/]""")


xp_temp = "==========================================60%======----------------------------"


def cria_monstro(inimigo):
    if inimigo.tipo == "Fogo":
        CORES["monstro"] = "dark_red"
        CORES["projetil"] = "orange_red1"

    elif inimigo.tipo == "Gelo":
        CORES["monstro"] = "blue"
        CORES["projetil"] = "bright_cyan"

    if inimigo.nome == "Mago":
        monstro = criar_mago()

    return monstro

def avanco_personagem(inimigo):
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
        
        console.print(Panel(cena, title=f"[bold green]{xp_temp}", border_style="purple", width=140))
        time.sleep(0.6)
        console.clear()


def personagem_atingido(inimigo):
    
    borda = "red"
    CORES["personagem"] = "bold red"

    muda_personagem_estado(inimigo, borda)


def esquiva_personagem(inimigo):

    borda = "blue"
    CORES["personagem"] = "bold blue"

    muda_personagem_estado(inimigo, borda)


def contaAtaque_personagem(inimigo):

    borda = "yellow"
    CORES["personagem"] = "bold yellow"


def tomarPocao_personagem(inimigo):

    borda = "green"
    CORES["personagem"] = "bold green"


def muda_personagem_estado(inimigo, borda):
    # Personagem toma dano
    console.clear()

    monstro = cria_monstro(inimigo)
    personagem = criar_personagem()

    cena_dano = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena_dano.append(linha_m)
        cena_dano.append(' ' * 100)
        cena_dano.append(linha_p)
        cena_dano.append('\n')

    console.print(Panel(cena_dano, title=f"[bold green]{xp_temp}", border_style=borda, width=140))
    time.sleep(1)
    CORES["personagem"] = "aquamarine1"

    voltar_normal(inimigo)


def ataque_monstro(inimigo):
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
                cena.append(' ' * (100 - pos))
                cena.append(linha_p)
                cena.append('\n')
            else:
                cena.append(linha_m)
                cena.append(' ' * (pos + 1))
                cena.append(' ' * (100 - pos))
                cena.append(linha_p)
                cena.append('\n')
      
        console.print(Panel(cena, title=f"[bold green]{xp_temp}", border_style="purple", width=140))
        time.sleep(0.7)
        console.clear()


def monstro_atingido(inimigo):
    # Monstro toma dano
    console.clear()
    
    monstro = cria_monstro(inimigo)

    aux = CORES["monstro"]
    CORES["monstro"] = "red1"

    if inimigo.nome == "Mago":
        monstro = criar_mago()

    personagem = criar_personagem()

    cena_dano = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena_dano.append(linha_m)
        cena_dano.append(' ' * 100)
        cena_dano.append(linha_p)
        cena_dano.append('\n')

    console.print(Panel(cena_dano, title=f"[bold green]{xp_temp}", subtitle="[bold red]MONSTRO ATINGIDO", border_style="red", width=140))
    time.sleep(1)

    CORES["monstro"] = aux
    voltar_normal(inimigo)


def voltar_normal(inimigo):
    # Volta ao normal
    console.clear()

    monstro = cria_monstro(inimigo)

    personagem = criar_personagem()

    cena_normal = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena_normal.append(linha_m)
        cena_normal.append(' ' * 100)
        cena_normal.append(linha_p)
        cena_normal.append('\n')

    console.print(Panel(cena_normal, title=f"[bold green]{xp_temp}", border_style="purple", width=140))
    time.sleep(0.6)
    console.clear()