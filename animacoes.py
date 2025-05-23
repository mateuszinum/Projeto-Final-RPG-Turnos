import time
from rich.text import Text
from rich.panel import Panel
from rich.console import Console

console = Console()     

CORES = {
    "monstro": "dark_red",
    "personagem": "aquamarine1",
    "projétil": "orange1",
    "dano": "bold red"
}

def criar_monstro():
    return Text.from_markup(
rf"""[bold {CORES["monstro"]}]
    O
   /|\
   / \
[/]""")

def criar_personagem():
    return Text.from_markup(
rf"""[bold {CORES["personagem"]}]
   \O/
    |
   / \
[/]""")

def criar_personagem_atingido():
    return Text.from_markup(
rf"""[bold {CORES["dano"]}]
   \O/
    |
   / \
[/]""")

xp_temp = "==========================================60%======----------------------------"

def ataque_persoanagem(): # botar pra receber o personagem e o inimigo
  # Ataque do Personagem
  for padding in [120, 90, 50, 20, 50, 90, 120]:
      monstro = criar_monstro()
      personagem = criar_personagem()
      
      cena = Text()
      for linha_m, linha_p in zip(monstro.split(), personagem.split()):
          cena.append(linha_m)
          cena.append(' ' * padding)
          cena.append(linha_p)
          cena.append('\n')
      
      console.print(Panel(cena, title=f"[bold green]{xp_temp}", border_style="purple", width=140))
      time.sleep(0.6)
      console.clear()

def ataque_monstro(): # botar pra receber o personagem e o inimigo
  # Ataque do Monstro
  for pos in [20, 50, 90, 120]:
      monstro = criar_monstro()
      personagem = criar_personagem()
      
      cena = Text()
      for i, (linha_m, linha_p) in enumerate(zip(monstro.split(), personagem.split())):
          if i == 2:
              cena.append(linha_m)
              cena.append(' ' * pos)
              cena.append(Text("▶", style=CORES["projétil"]))
              cena.append(' ' * (120 - pos))
              cena.append(linha_p)
              cena.append('\n')
          else:
              cena.append(linha_m)
              cena.append(' ' * (pos + 1))
              cena.append(' ' * (120 - pos))
              cena.append(linha_p)
              cena.append('\n')
      
      console.print(Panel(cena, title=f"[bold green]{xp_temp}", border_style="purple", width=140))
      time.sleep(0.6)
      console.clear()


def personagem_atingido(): # botar pra receber o personagem e o inimigo
  # Personagem toma dano
  monstro = criar_monstro()
  personagem = criar_personagem_atingido()

  cena_dano = Text()
  for linha_m, linha_p in zip(monstro.split(), personagem.split()):
      cena_dano.append(linha_m)
      cena_dano.append(' ' * 123)
      cena_dano.append(linha_p)
      cena_dano.append('\n')

  console.print(Panel(cena_dano, title=f"[bold green]{xp_temp}", border_style="red", width=140))
  time.sleep(0.6)


def volta_ao_normal(): # botar pra receber o personagem e o inimigo
  # Volta ao normal
  console.clear()
  monstro = criar_monstro()
  personagem = criar_personagem()

  cena_normal = Text()
  for linha_m, linha_p in zip(monstro.split(), personagem.split()):
      cena_normal.append(linha_m)
      cena_normal.append(' ' * 123)
      cena_normal.append(linha_p)
      cena_normal.append('\n')

  console.print(Panel(cena_normal, title=f"[bold green]{xp_temp}", border_style="purple", width=140))