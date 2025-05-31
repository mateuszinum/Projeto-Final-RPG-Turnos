from sql import cursor, conexao
from personagens import tanque, cavaleiro, assassino

def resetar_banco_de_dados():
    tabelas = ["Historico", "Turnos", "Jogos", "Inimigos"]
    for tabela in tabelas:
        cursor.execute(f"DELETE FROM {tabela}")
    
    herois_padrao = {
        "Tanque": tanque,
        "Cavaleiro": cavaleiro,
        "Assassino": assassino
    }

    cursor.execute("SELECT Nome FROM Personagens")
    nomes = cursor.fetchall()

    for (nome,) in nomes:
        if nome in herois_padrao:
            h = herois_padrao[nome]
            cursor.execute("""
                UPDATE Personagens
                SET Vida = ?, Ataque = ?, Defesa = ?, Velocidade = ?, Level = ?, XP_Atual = ?, Pocoes = ?, Chave = ?
                WHERE Nome = ?
            """, ( h.vida_max, h.ataque, h.defesa_inicial, h.velocidade, 1, 0, h.pocoes_max, 0, nome)
            )

    conexao.commit()
