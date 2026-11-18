import customtkinter as ctk

def cadastrar_emprestimo(Janela_filho):
    emp = ctk.CTkToplevel(Janela_filho)
    emp.title("Cadastrar empréstimo")
    emp.geometry("600x600")
    ctk.set_appearance_mode("System")

    leitores = ["João", "Tereza", "José", "Marcos", "Joana"]

    label_leitor = ctk.CTkLabel(emp, text='Selecione o leitor:')
    label_leitor.pack(pady=(15, 0))

    Lista_leitor = ctk.CTkOptionMenu(emp, values=leitores ,width=300)
    Lista_leitor.set("Selecione")
    Lista_leitor.pack(pady=5)

    livros = ["Harry potter e pedra filosofal", "Dom casmurro", "O Guarani", "Dicionario de português", "Apostila do curso técnico 2026"]

    label_leitor = ctk.CTkLabel(emp, text='Selecione o livro:')
    label_leitor.pack(pady=(15, 0))
    
    Lista_livro = ctk.CTkOptionMenu(emp, values=livros ,width=300)
    Lista_livro.set("Selecione")
    Lista_livro.pack(pady=5)

    label_entrega = ctk.CTkLabel(emp, text='Dia de entrega do Livro')
    label_entrega.pack(pady=(0, 0))
    campo_entrega = ctk.CTkEntry(emp, placeholder_text='Digite no formato Dia/Mês/Ano',width=200)
    campo_entrega.pack(pady=0)

    label_dev = ctk.CTkLabel(emp, text='Devolução dia')
    label_dev.pack(pady=(0, 0))
    campo_dev = ctk.CTkEntry(emp, placeholder_text='Digite no formato Dia/Mês/Ano',width=200)
    campo_dev.pack(pady=0)

    botao = ctk.CTkButton(emp, text="cadastrar")
    botao.pack(pady=5)

    emp.mainloop()



