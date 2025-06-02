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


def criar_mago_ascii():
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


def criar_fenix_ascii():
    return Text.from_markup(
rf"""[bold {CORES["monstro"]}]
 .\\            //.
. \ \          / /.
.\  ,\     /` /,.- 
 -.   \  /'/ /  .  
 ` -   `-'  \  -   
   '.       /.\`   
      -    .-      
      :`//.'       
      .`.'         
      .'           
[/]""")


def criar_guardiao_ascii():
    return Text.from_markup(
rf"""[bold {CORES["monstro"]}]
               _____     
     _____    /__ /(      
    /  _  \    `. \ \     
   |  [ () |     \ \ \    
 .---.    ¯|-..   \ \  \  
//` \ \¯¯¯¯¯\  \  _// \ | 
\` ,' /     )  / (,`|`--' 
 `---´     `/-´`.// /     
  |  \  '|'( \  // /      
  \  | _  _|  `// /       
[/]""")


def criar_demonio_ascii():
    return Text.from_markup(
rf"""[bold {CORES["monstro"]}]
          v  
    (__)v | v
    /\/\\_|_/
   _\__/  |  
  /  \/`\<`) 
  \ (  |\_/  
  /)))-(  |  
 / /^ ^ \ |  
/  )^/\^( |  
)_//`__>> |  
  #   #`  |  
[/]""")


def criar_personagem_ascii():
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


def cria_monstro_ascii(inimigo):
    if inimigo.tipo == "Fogo":
        CORES["monstro"] = "indian_red"
        CORES["projetil"] = "dark_orange"

    elif inimigo.tipo == "Gelo":
        CORES["monstro"] = "cornflower_blue"
        CORES["projetil"] = "deep_sky_blue1"

    if inimigo.nome == "Mago":
        monstro = criar_mago_ascii()
    elif inimigo.nome == "Fênix":
        monstro = criar_fenix_ascii()
    elif inimigo.nome == "Guardião Elemental":
        monstro = criar_guardiao_ascii()
    elif inimigo.nome == "Demônio":
        monstro = criar_demonio_ascii()

    return monstro


# Cena estática
def criar_cena(heroi, inimigo):
    console.clear()

    monstro = cria_monstro_ascii(inimigo)
    personagem = criar_personagem_ascii()

    if inimigo.nome == "Mago":
        pos = 100
    elif inimigo.nome == "Fênix":
        pos = 95
    elif inimigo.nome == "Guardião Elemental":
        pos = 90
    elif inimigo.nome == "Demônio":
        pos = 105

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * pos)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))


def avanco_personagem(heroi, inimigo):
    # Ataque do Personagem
    console.clear()

    monstro = cria_monstro_ascii(inimigo)
    personagem = criar_personagem_ascii()

    if inimigo.nome == "Mago":
        posicoes = [100, 80, 60, 40, 60, 80, 100]
    elif inimigo.nome == "Fênix":
        posicoes = [95, 80, 60, 40, 60, 80, 95]
    elif inimigo.nome == "Guardião Elemental":
        posicoes = [90, 70, 50, 30, 50, 70, 90]
    elif inimigo.nome == "Demônio":
        posicoes = [105, 85, 65, 45, 65, 85, 105]

    for pos in posicoes:
        
        cena = Text()
        for linha_m, linha_p in zip(monstro.split(), personagem.split()):
            cena.append(linha_m)
            cena.append(' ' * pos)
            cena.append(linha_p)
            cena.append('\n')
        
        console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))
        time.sleep(0.4)
        console.clear()


def personagem_atingido(heroi, inimigo):
    
    borda = "red1"
    CORES["personagem"] = "red1"

    muda_personagem_estado(heroi, inimigo, borda)


def esquiva_personagem(heroi, inimigo):

    borda = "dodger_blue2"
    CORES["personagem"] = "dodger_blue2"

    muda_personagem_estado(heroi, inimigo, borda)


def contraAtaque_personagem(heroi, inimigo):

    borda = "dark_orange3"
    CORES["personagem"] = "dark_orange3"

    muda_personagem_estado(heroi, inimigo, borda)


def bloqueio_personagem(heroi, inimigo):

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

    monstro = cria_monstro_ascii(inimigo)
    personagem = criar_personagem_ascii()

    if inimigo.nome == "Mago":
        pos = 100
    elif inimigo.nome == "Fênix":
        pos = 95
    elif inimigo.nome == "Guardião Elemental":
        pos = 90
    elif inimigo.nome == "Demônio":
        pos = 105

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * pos)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style=borda, width=140))
    time.sleep(1)
    CORES["personagem"] = "grey46"

    voltar_normal(heroi, inimigo)


def ataque_monstro(heroi, inimigo):
    # Ataque do Monstro
    console.clear()

    if inimigo.nome == "Mago":
        posicoes = [40, 60, 80]
        num = 100
    elif inimigo.nome == "Fênix":
        posicoes = [30, 50, 70]
        num = 95
    elif inimigo.nome == "Guardião Elemental":
        posicoes = [40, 60, 80]
        num = 90
    elif inimigo.nome == "Demônio":
        posicoes = [45, 65, 85]
        num = 105

    for pos in posicoes:
        
        monstro = cria_monstro_ascii(inimigo)

        personagem = criar_personagem_ascii()
        
        cena = Text()
        for i, (linha_m, linha_p) in enumerate(zip(monstro.split(), personagem.split())):
            if i == 5:
                cena.append(linha_m)
                cena.append(' ' * pos)
                cena.append(Text("▶", style=CORES["projetil"]))
                cena.append(Text("▶", style=CORES["projetil"]))
                cena.append(' ' * ((num - 1) - pos))
                cena.append(linha_p)
                cena.append('\n')
            else:
                cena.append(linha_m)
                cena.append(' ' * (pos + 1))
                cena.append(' ' * (num - pos))
                cena.append(linha_p)
                cena.append('\n')
      
        console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))
        time.sleep(0.6)
        console.clear()


def monstro_atingido(heroi, inimigo):
    # Monstro toma dano
    console.clear()

    aux = CORES["monstro"]
    CORES["monstro"] = "red1"

    if inimigo.nome == "Mago":
        monstro = criar_mago_ascii()
    elif inimigo.nome == "Fênix":
        monstro = criar_fenix_ascii()
    elif inimigo.nome == "Guardião Elemental":
        monstro = criar_guardiao_ascii()
    elif inimigo.nome == "Demônio":
        monstro = criar_demonio_ascii()

    personagem = criar_personagem_ascii()

    if inimigo.nome == "Mago":
        pos = 100
    elif inimigo.nome == "Fênix":
        pos = 95
    elif inimigo.nome == "Guardião Elemental":
        pos = 90
    elif inimigo.nome == "Demônio":
        pos = 105

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * pos)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{aux}]{vida_monstro(inimigo)}", border_style=f"{CORES['monstro']}", width=140))
    time.sleep(1)

    CORES["monstro"] = aux
    voltar_normal(heroi, inimigo)


def voltar_normal(heroi, inimigo):
    # Volta ao normal
    console.clear()

    monstro = cria_monstro_ascii(inimigo)
    personagem = criar_personagem_ascii()

    if inimigo.nome == "Mago":
        pos = 100
    elif inimigo.nome == "Fênix":
        pos = 95
    elif inimigo.nome == "Guardião Elemental":
        pos = 90
    elif inimigo.nome == "Demônio":
        pos = 105

    cena = Text()
    for linha_m, linha_p in zip(monstro.split(), personagem.split()):
        cena.append(linha_m)
        cena.append(' ' * pos)
        cena.append(linha_p)
        cena.append('\n')

    console.print(Panel(cena, title=f"[bright_green]{vida_heroi(heroi)}", subtitle=f"[{CORES['monstro']}]{vida_monstro(inimigo)}", border_style="medium_orchid", width=140))
    time.sleep(0.6)
    console.clear()