from classes import *

tanque = Personagem(
    nome="Tanque",
    vida=350,
    ataque=20,
    defesa=50,
    velocidade=10,
    level=1,
    arma=Arma(nome='Clava', dano=10, critico=5),
    qnt_pocoes=3,
    chave=False
)

cavaleiro = Personagem(
    nome="Cavaleiro",
    vida=250,
    ataque=30,
    defesa=30,
    velocidade=20,
    level=1,
    arma=Arma(nome='Espada', dano=15, critico=10),
    qnt_pocoes=3,
    chave=False
)

assassino = Personagem(
    nome="Assassino",
    vida=150,
    ataque=40,
    defesa=10,
    velocidade=40,
    level=1,
    arma=Arma(nome='Adaga', dano=25, critico=25),
    qnt_pocoes=2,
    chave=False
)

def criar_monstro(inimigo):
    if inimigo == "Mago":
        return Inimigo(
            nome="Mago",
            raca="Mago",
            tipo = ["Fogo", "Gelo"],
            vida=100,
            ataque=15,
            defesa=10,
            velocidade=25,
            level=1,
            arma=Arma(nome='Cajado', dano=15, critico=15),
            qnt_pocoes=0,
            chave=random.choices([True, False], weights=[10, 90])[0]
        )

    elif inimigo == "Fenix":
        return Inimigo(
            nome="Fênix",
            raca="Fênix",
            tipo = ["Fogo", "Gelo"],
            vida=300,
            ataque=30,
            defesa=20,
            velocidade=30,
            level=2,
            arma=Arma(nome='Bico', dano=25, critico=5),
            qnt_pocoes=0,
            chave=random.choices([True, False], weights=[40, 60])[0]
        )

    elif inimigo == "Guardiao":
        return Inimigo(
            nome="Guardião Elemental",
            raca="Guardião Elemental",
            tipo = ["Fogo", "Gelo"],
            vida=500,
            ataque=30,
            defesa=20,
            velocidade=30,
            level=3,
            arma=Arma(nome='Martelo Mágico', dano=25, critico=5),
            qnt_pocoes=0,
            chave=random.choices([True, False], weights=[80, 20])[0]
        )

    elif inimigo == "Demonio":
        return Inimigo(
            nome="Demônio",
            raca="Demônio",
            tipo = ["Fogo", "Gelo"],
            vida=1500,
            ataque=70,
            defesa=40,
            velocidade=50,
            level=5,
            arma=Arma(nome='Tridente', dano=55, critico=25),
            qnt_pocoes=0,
            chave=False
        )
