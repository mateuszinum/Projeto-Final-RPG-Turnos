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