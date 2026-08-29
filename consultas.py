import sqlite3

conexao = sqlite3.connect("estagios.db")

cursor = conexao.cursor()

def listar_vagas (area = None, prazo = None, sem_prazo = False):
    condicoes = []
    valores = []

    if area is not None:
        condicoes.append("vaga_area = ?")
        valores.append(area)
    if prazo is not None:
        condicoes.append("vaga_prazo_final <= ? and vaga_prazo_final !=''")
        valores.append(prazo)
    elif sem_prazo:
        condicoes.append("vaga_prazo_final = ''")

    query = "SELECT * FROM vaga"
    if condicoes:
        query += " WHERE " + " AND ". join(condicoes)
    
    print(query)
    cursor.execute(query, valores)

    return cursor.fetchall()

