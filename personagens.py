from classes import *


def criar_monstro(inimigo):
    if inimigo == "Mago":
        sorteio = random.choices([True, False], weights=[10, 90])[0]
        return Inimigo(
            nome="Mago",
            raca="Mago",
            tipo = ["Fogo", "Gelo"],
            vida=100,
            ataque=15,
            defesa=10,
            velocidade=25,
            xp_atual=0,
            level=1,
            arma=Arma(nome='Cajado', dano=15, critico=15),
            qnt_pocoes=0,
            chave=sorteio
        )

    elif inimigo == "Fenix":
        sorteio = random.choices([True, False], weights=[40, 60])[0]
        return Inimigo(
            nome="Fênix",
            raca="Fênix",
            tipo = ["Fogo", "Gelo"],
            vida=300,
            ataque=30,
            defesa=20,
            velocidade=30,
            xp_atual=0,
            level=2,
            arma=Arma(nome='Bico', dano=25, critico=5),
            qnt_pocoes=0,
            chave=sorteio
        )

    elif inimigo == "Guardiao":
        sorteio = random.choices([True, False], weights=[80, 20])[0]
        return Inimigo(
            nome="Guardião Elemental",
            raca="Guardião Elemental",
            tipo = ["Fogo", "Gelo"],
            vida=500,
            ataque=30,
            defesa=20,
            velocidade=30,
            xp_atual=0,
            level=3,
            arma=Arma(nome='Martelo Mágico', dano=25, critico=5),
            qnt_pocoes=0,
            chave=sorteio
        )

    elif inimigo == "Demonio":
        return Inimigo(
            nome="Demônio",
            raca="Demônio",
            tipo = ["Fogo", "Gelo"],
            vida=700,
            ataque=70,
            defesa=40,
            velocidade=50,
            xp_atual=0,
            level=6,
            arma=Arma(nome='Tridente', dano=55, critico=25),
            qnt_pocoes=0,
            chave=False
        )