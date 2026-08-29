import sqlite3
import csv

conexao = sqlite3.connect("estagios.db")
cursor = conexao.cursor()

def converter_data (data):
    if data:
        return data[6:10] + "-" + data[3:5] + "-" + data[0:2]
    return ""

with open ("empresa.csv", encoding = "latin-1") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter = ";")
    for linha in leitor:
        cursor.execute(
            "INSERT INTO empresa (emp_id, emp_nome) VALUES (?, ?)", (linha ["id"], linha["nome"])
        )

with open ("vaga.csv", encoding = "latin-1") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter = ";")
    for linha in leitor:
        cursor.execute(
            "INSERT INTO vaga (vaga_id, emp_id, vaga_area, vaga_prazo_final, vaga_link, vaga_modelo_trabalho)  VALUES (?, ?, ?, ?, ?, ?)", (linha ["id"], linha["empresa_id"], linha["area"], converter_data(linha["prazo_final"]), linha["link"], linha["modelo_trabalho"])
        )

conexao.commit()
conexao.close()