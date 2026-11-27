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

def cadastrar_usuario(nome_usuario, cpf, email, senha, instituicao):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO aluno (instituicao)
            VALUES (?)
        """, (instituicao,))
        
        id_aluno = cursor.lastrowid
        
        cursor.execute("""
            INSERT INTO usuario (id_aluno, nome_usuario, cpf, email, senha)
            VALUES (?, ?, ?, ?, ?)
        """, (id_aluno, nome_usuario, cpf, email, senha))
        
        conexao.commit()
        return True, "Usuario Cadastrado com Sucesso" 
    except Exception as erro:
        conexao.rollback()
        return False, f"Usuario não cadastrado erro: {erro}"
    finally:
        conexao.close()

def lista_leitor():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id_aluno, nome_usuario
        FROM usuario
        WHERE id_aluno IS NOT NULL
        ORDER BY nome_usuario
    """)
    leitores = cursor.fetchall()
    conexao.close()
    return leitores

def lista_livros():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id_livro, titulo
        FROM livro
        ORDER BY titulo
    """)
    livros = cursor.fetchall()
    conexao.close()
    return livros


