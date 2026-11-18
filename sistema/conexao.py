import sqlite3 as sql

Bd = "banco.db"

def conectar():
    conexao = sql.connect(Bd)
    conexao.execute("PRAGMA foreign_key = on;")
    return conexao

