import sqlite3

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Personagens (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Vida INTEGER,
        Ataque INTEGER,
        Defesa INTEGER,
        Velocidade INTEGER,
        Arma TEXT NOT NULL,
        Pocoes INTEGER
    )                     
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inimigos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Personagem_ID INTEGER,
        Raca TEXT NOT NULL,
        Tipo TEXT NOT NULL
        FOREIGN KEY (Personagem_ID) REFERENCES Personagens(ID)
    )                            
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Jogos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Heroi_ID INTEGER,
        Inimigo_ID INTEGER,
        Vencedor INTEGER,
        FOREIGN KEY (Heroi_ID) REFERENCES Personagens(ID),
        FOREIGN KEY (Inimigo_ID) REFERENCES Inimigos(ID)
    )               
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Turnos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Heroi_ID INTEGER,
        Inimigo_ID INTEGER,
        Acao TEXT NOT NULL,
        Autor TEXT NOT NULL,
        Sucesso INTEGER,
        FOREIGN KEY (Heroi_ID) REFERENCES Personagens(ID),
        FOREIGN KEY (Inimigo_ID) REFERENCES Inimigos(ID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Historico (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Jogo_ID INTEGER,
        Turno_ID INTEGER,
        Vida_Heroi INTEGER,
        Vida_Inimigo INTEGER,
        FOREIGN KEY (Jogo_ID) REFERENCES Jogos(ID),
        FOREIGN KEY (Turno_ID) REFERENCES Turnos(ID)
    )
''')

conexao.commit()

def insert_personagem_e_retorna_id(personagem):
    cursor.execute("INSERT INTO Personagens (Nome, Vida, Ataque, Defesa, Velocidade, Arma, Pocoes) VALUES (?, ?, ?, ?, ?, ?, ?)", (personagem.nome, personagem.vida_max, personagem.ataque, personagem.defesa_inicial, personagem.velocidade, personagem.arma, personagem.pocoes))
    
    conexao.commit()
    
    return cursor.lastrowid

def insert_inimigo_e_retorna_id(inimigo):
    inimigo_id = insert_personagem_e_retorna_id(inimigo)
    
    cursor.execute("INSERT INTO Inimigos (Personagem_ID, Raca, Tipo) VALUES (?, ?, ?)", (inimigo_id, inimigo.raca, inimigo.tipo))
    
    conexao.commit()    
    
    return cursor.lastrowid

def insert_jogo_e_retorna_id(heroi_id, inimigo_id):
    cursor.execute("INSERT INTO Jogos (Heroi_ID, Inimigo_ID, Vencedor) VALUES (?, ?, ?)", (heroi_id, inimigo_id, None))

    conexao.commit()

    return cursor.lastrowid

def insert_turno_e_retorna_id(heroi_id, inimigo_id, acao, autor, sucesso):
    if sucesso:
        cursor.execute("INSERT INTO Turnos (Heroi_ID, Inimigo_ID, Acao, Autor, Sucesso) VALUES (?, ?, ?, ?, ?)", (heroi_id, inimigo_id, acao, autor, 1))
    
    else:  
        cursor.execute("INSERT INTO Turnos (Heroi_ID, Inimigo_ID, Acao, Autor, Sucesso) VALUES (?, ?, ?, ?, ?)", (heroi_id, inimigo_id, acao, autor, 0))
    
    conexao.commit()
    
    return cursor.lastrowid

def insert_historico(jogo_id, turno_id, vida_heroi, vida_inimigo):
    cursor.execute("INSERT INTO Historico (Jogo_ID, Turno_ID, Vida_Heroi, Vida_Inimigo) VALUES (?, ?, ?, ?)", (jogo_id, turno_id, vida_heroi, vida_inimigo))
    
    conexao.commit()