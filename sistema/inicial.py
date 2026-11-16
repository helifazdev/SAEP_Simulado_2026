import customtkinter as ctk
from sistema.livro import cadastrar_livro

def exibir_inicial():
    ini = ctk.CTk()
    ini.title("Página inicial - Adm")
    ini.geometry("500x400")

    label_titulo = ctk.CTkLabel(ini, text="PAINEL DO BIBLIOTECÁRIO")
    label_titulo.pack(pady=30)

    btn_leitor = ctk.CTkButton(ini, text="Cadastrar Leitor")
    btn_leitor.pack(pady=15)

    btn_livro = ctk.CTkButton(ini, text="Cadastrar Livro", command=lambda:(cadastrar_livro(ini)))
    btn_livro.pack(pady=15)

    btn_emprestimo = ctk.CTkButton(ini, text="Empréstimos")
    btn_emprestimo.pack(pady=15)

    ini.mainloop()
