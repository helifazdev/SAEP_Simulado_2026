import sqlite3 as sql
import customtkinter as ctk

Bd = "banco.db"

def conectar():
    conexao = sql.connect(Bd)
    conexao.execute("PRAGMA foreign_key = on;")
    return conexao

def autenticar_usuario(login, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
       SELECT id_bibliotecario, id_aluno 
       FROM usuario
       WHERE (nome_usuario = ?) AND senha = ?     
    """, (login, senha))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        id_bibliotecario, id_aluno = resultado
        if id_bibliotecario is not None:
            return "bibliotecario"
        if id_aluno is not None:
            return "leitor"
    return None

def cadastrar_livro(titulo, autor, editora, isbn, ano_publicacao, edicao):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
        INSERT INTO livro(titulo, autor, editora, isbn, ano_publicacao, edicao) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, 
        (titulo, autor, editora, isbn, ano_publicacao, edicao)
                       )
        conexao.commit()
        return True, "Livro cadastrado com Sucesso!" 
    except Exception as erro:
        conexao.rollback()
        return False, f"Livro não cadastrado erro:{erro}"
    finally:
        conexao.close()

def cadastrar_usuario(nome_usuario, cpf, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
        INSERT INTO usuario (nome_usuario, cpf, email, senha)
        VALUES (?, ?, ?, ?, ?)
    """, (nome_usuario, cpf, email, senha))
        conexao.commit()
        return True, "Usuario Cadastrado com Sucesso" 
    except Exception as erro:
        conexao.rollback()
        return False, f"Livro não cadastrado erro:{erro}"
    finally:
        conexao.close()





