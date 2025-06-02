import time
from classes import Personagem, Arma
from sql import cursor

def obter_herois():
    nomes = ["Tanque", "Cavaleiro", "Assassino"]

    herois = {}
    
    for nome_base in nomes:
        cursor.execute(f"""
            SELECT ID, Nome, Vida, Ataque, Defesa, Velocidade, Arma, Pocoes, Level, XP_Atual, Chave
            FROM Personagens
            WHERE Nome LIKE ?
            ORDER BY ID DESC
            LIMIT 1
        """, (f"{nome_base}%",))

        resultado = cursor.fetchone()

        if resultado:
            (
                id_,
                nome,
                vida,
                ataque,
                defesa,
                velocidade,
                arma_nome,
                pocoes,
                level,
                xp_atual,
                chave
            ) = resultado

            arma_padrao = {
                "Clava": Arma("Clava", 10, 5),
                "Espada": Arma("Espada", 15, 10),
                "Adaga": Arma("Adaga", 25, 25)
            }

            arma = arma_padrao.get(arma_nome, Arma(arma_nome, 10, 5))

            herois[nome_base] = Personagem(
                nome=nome,
                vida=vida,
                ataque=ataque,
                defesa=defesa,
                velocidade=velocidade,
                xp_atual=xp_atual,
                level=level,
                arma=arma,
                qnt_pocoes=pocoes,
                chave=bool(chave),
                )

    return herois["Tanque"], herois["Cavaleiro"], herois["Assassino"]

obter_herois()

def criar_personagem_novo():

    tanque = Personagem(
            nome=f"Tanque_{int(time.time())}",
            vida=350,
            ataque=20,
            defesa=50,
            velocidade=10,
            xp_atual=0,
            level=1,
            arma=Arma("Clava", 10, 5),
            qnt_pocoes=3,
            chave=False
        )

    cavaleiro = Personagem(
            nome=f"Cavaleiro_{int(time.time())}",
            vida=250,
            ataque=30,
            defesa=30,
            velocidade=20,
            xp_atual=0,
            level=1,
            arma=Arma("Espada", 15, 10),
            qnt_pocoes=3,
            chave=False
        )

    assassino = Personagem(
            nome=f"Assassino_{int(time.time())}",
            vida=150,
            ataque=40,
            defesa=10,
            velocidade=40,
            xp_atual=0,
            level=1,
            arma=Arma("Adaga", 25, 25),
            qnt_pocoes=2,
            chave=False
        )
    
    return tanque, cavaleiro, assassino