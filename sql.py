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
        Pocoes INTEGER,
        Level INTEGER DEFAULT 1,
        XP_Atual INTEGER DEFAULT 0,
        Chave INTEGER DEFAULT 0
    )                     
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inimigos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Personagem_ID INTEGER,
        Raca TEXT NOT NULL,
        Tipo TEXT NOT NULL,
        FOREIGN KEY (Personagem_ID) REFERENCES Personagens(ID) ON DELETE CASCADE
    )                            
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Jogos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Heroi_ID INTEGER,
        Inimigo_ID INTEGER,
        Vencedor_ID INTEGER,
        Vencedor_Tipo TEXT,
        FOREIGN KEY (Heroi_ID) REFERENCES Personagens(ID) ON DELETE SET NULL,
        FOREIGN KEY (Inimigo_ID) REFERENCES Inimigos(ID) ON DELETE SET NULL
    )                
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Turnos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Heroi_ID INTEGER,
        Inimigo_ID INTEGER,
        Acao_ID INTEGER,
        Autor_ID INTEGER,
        Autor_Tipo TEXT NOT NULL,
        Sucesso INTEGER,
        FOREIGN KEY (Heroi_ID) REFERENCES Personagens(ID) ON DELETE CASCADE,
        FOREIGN KEY (Inimigo_ID) REFERENCES Inimigos(ID) ON DELETE CASCADE,
        FOREIGN KEY (Acao_ID) REFERENCES Acoes(ID)
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Historico (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Jogo_ID INTEGER,
        Turno_ID INTEGER,
        Vida_Heroi INTEGER,
        Vida_Inimigo INTEGER,
        FOREIGN KEY (Jogo_ID) REFERENCES Jogos(ID) ON DELETE CASCADE,
        FOREIGN KEY (Turno_ID) REFERENCES Turnos(ID) ON DELETE CASCADE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Acoes (
        ID INTEGER,
        Nome TEXT NOT NULL
    )
''')

cursor.execute("SELECT 1 FROM Acoes LIMIT 1")
elemento_1 = cursor.fetchone()

if elemento_1 is None:
    for i in range(1, 6):
        acao = {
            1: "Ataque",
            2: "Esquiva",
            3: "Contra Ataque",
            4: "Pocao",
            5: "Defesa"
        }
        cursor.execute("INSERT INTO Acoes (ID, Nome) VALUES (?, ?)", (i, acao[i]))

        conexao.commit()




def insert_personagem_e_retorna_id(personagem):
    cursor.execute("""
        INSERT INTO Personagens (Nome, Vida, Ataque, Defesa, Velocidade, Arma, Pocoes, Level, XP_Atual, Chave)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        personagem.nome,
        personagem.vida_max,
        personagem.ataque,
        personagem.defesa_inicial,
        personagem.velocidade,
        personagem.arma.nome,
        personagem.pocoes_max,
        personagem.level,
        personagem.xp_atual,
        int(personagem.chave)
    ))  
    conexao.commit()
    
    return cursor.lastrowid

def carregar_dados_personagem_completo(nome):
    cursor.execute("""
        SELECT Vida, Ataque, Defesa, Velocidade, Pocoes, Level, XP_Atual, Chave
        FROM Personagens
        WHERE Nome = ?
    """, (nome,))
    return cursor.fetchone()


def insert_inimigo_e_retorna_id(inimigo):
    
    cursor.execute("INSERT INTO Inimigos (Personagem_ID, Raca, Tipo) VALUES (?, ?, ?)", (inimigo.id, inimigo.raca, inimigo.tipo))
    
    conexao.commit()    
    
    return cursor.lastrowid


def insert_jogo_e_retorna_id(heroi_id, inimigo_id):
    cursor.execute("INSERT INTO Jogos (Heroi_ID, Inimigo_ID, Vencedor_ID, Vencedor_Tipo) VALUES (?, ?, ?, ?)", (heroi_id, inimigo_id, None, None))

    conexao.commit()

    return cursor.lastrowid

def atualiza_vencedor_jogo(jogo_id, vencedor_id, vencedor_tipo):
    cursor.execute("""
        UPDATE Jogos
        SET Vencedor_ID = ?, Vencedor_Tipo = ?
        WHERE ID = ?
""", (vencedor_id, vencedor_tipo, jogo_id))
    
    conexao.commit()


def insert_turno_e_retorna_id(heroi_id, inimigo_id, acao_id, autor_id, autor_tipo, sucesso):
    cursor.execute("INSERT INTO Turnos (Heroi_ID, Inimigo_ID, Acao_ID, Autor_ID, Autor_Tipo, Sucesso) VALUES (?, ?, ?, ?, ?, ?)", (heroi_id, inimigo_id, acao_id, autor_id, autor_tipo, int(sucesso)))   
    conexao.commit()
    
    return cursor.lastrowid


def insert_historico(jogo_id, turno_id, vida_heroi, vida_inimigo):
    cursor.execute("INSERT INTO Historico (Jogo_ID, Turno_ID, Vida_Heroi, Vida_Inimigo) VALUES (?, ?, ?, ?)", (jogo_id, turno_id, vida_heroi, vida_inimigo))
    
    conexao.commit()

def personagem_existe_ou_inimigo(nome):
    if nome in ['Mago', 'Fenix', 'Guardiao', 'Demonio']:
        return False
    
    cursor.execute("SELECT ID FROM Personagens WHERE Nome = ?", (nome,))
    return cursor.fetchone() is not None

def atualiza_heroi(heroi_id, vida, ataque, defesa, velocidade, level, xp_atual, pocoes, chave):
    cursor.execute("""
        UPDATE Personagens
        SET Vida = ?, Ataque = ?, Defesa = ?, Velocidade = ?, Level = ?, XP_Atual = ?, Pocoes = ?, Chave = ?
        WHERE ID = ?
    """, (vida, ataque, defesa, velocidade, level, xp_atual, pocoes, int(chave), heroi_id))

    conexao.commit()

def ha_jogos_salvos():
    cursor.execute("SELECT COUNT(*) FROM Jogos")
    return cursor.fetchone()[0] > 0

