import sqlite3

conexao = sqlite3.connect("estagios.db")

cursor = conexao.cursor()

criar_tabelas = """
CREATE TABLE empresa (
    emp_id integer primary key autoincrement,
    emp_nome text 
    );

CREATE TABLE vaga (
    vaga_id integer primary key autoincrement,
    vaga_area text,
    vaga_prazo_final text,
    vaga_link text,
    vaga_modelo_trabalho text,
    emp_id integer references empresa(emp_id) 
    );
"""
cursor.executescript(criar_tabelas)

conexao.commit()
conexao.close()