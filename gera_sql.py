import sqlite3 as sql

def exporta_sql():
    conexao = sql.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_key = ON;")
   
    with open ("saep_db.sql",'w', encoding="utf-8") as arquivo:
        for linha in conexao.iterdump():
            arquivo.write(f"{linha}\n")

        conexao.close()
        print("SQL processado com sucesso!")

exporta_sql()       
