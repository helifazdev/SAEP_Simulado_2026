# print("Hello, World!")
import sqlite3 as sql
conexao = sql.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_key = ON;")

def criar_banco_dados():
      
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS livro (
                        id_livro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        editora TEXT,
                        isbn TEXT UNIQUE,
                        ano_publicacao DATE NOT NULL,
                        edicao INTEGER
        );
        """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS aluno (
                    id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    instituicao TEXT NOT NULL
        );
        """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS bibliotecario (
                        id_bibliotecario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
        );
        """)

        cursor.execute(
              """
                CREATE TABLE IF NOT EXISTS usuario (
                    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_usuario TEXT NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    id_bibliotecario INTEGER,
                    id_aluno INTEGER,
                    FOREIGN KEY (id_bibliotecario) REFERENCES bibliotecario(id_bibliotecario) ON DELETE SET NULL,
                    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno) ON DELETE SET NULL

        );
         """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS emprestimo (
                    id_emprestimo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_livro INTEGER NOT NULL,
                    id_aluno INTEGER NOT NULL,
                    data_emprestimo DATE,
                    data_devolucao DATE,
                    FOREIGN KEY (id_livro) REFERENCES livro(id_livro),
                    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)  
        );
        """
                       )

        conexao.commit()
        conexao.close()
        print("Banco de dados concluído!!")

criar_banco_dados()



