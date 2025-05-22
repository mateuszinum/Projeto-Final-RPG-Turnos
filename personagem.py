from sistema import *

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

# Função: Alta chance de crítico, esquiva e contra-ataque.
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

# Função: Alto dano mágico (representado por ataque alto), mas frágil.
mago = Personagem(
    nome="Mago",
    vida=120,
    ataque=50,
    defesa=10,
    velocidade=25,
    level=1,
    arma_inicial=Arma(dano=30, critico=20),
    qnt_pocoes=3
)

arqueiro = Personagem(
    nome="Arqueiro",
    vida=180,
    ataque=28,
    defesa=20,
    velocidade=35,
    level=1,
    arma_inicial=Arma(dano=18, critico=22),
    qnt_pocoes=3
)
