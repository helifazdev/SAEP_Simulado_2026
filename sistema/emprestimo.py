import customtkinter as ctk
from sistema.conexao import lista_leitor, lista_livros
from datetime import date, timedelta

def cadastrar_emprestimo(Janela_filho):
    Janela_filho.withdraw()
    emp = ctk.CTkToplevel(Janela_filho)
    emp.title("Cadastrar empréstimo")
    emp.geometry("600x600")
    ctk.set_appearance_mode("System")

    leitores = lista_leitor()
    mapa_leitor = {f"{nome}": id_aluno for id_aluno, nome in leitores}
    opcoes_leitores = list(mapa_leitor.keys())if mapa_leitor else ["Nenhum aluno encontrado"]

    label_leitor = ctk.CTkLabel(emp, text='Selecione o leitor:')
    label_leitor.pack(pady=(15, 0))

    Lista_leitor = ctk.CTkOptionMenu(emp, values=opcoes_leitores ,width=300)
    Lista_leitor.set("Selecione")
    Lista_leitor.pack(pady=5)

    livros = lista_livros()
    mapa_livro = {f"{titulo}": id_livro for id_livro, titulo in livros}
    opcoes_livros = list(mapa_livro.keys())if mapa_livro else ["Nenhum livro cadastrado"]

    #----------Data de entrega e de devolução--------
    data_de_emprestimo = date.today()
    Data_devolução = data_de_emprestimo + timedelta(days=7) 

    label_leitor = ctk.CTkLabel(emp, text='Selecione o livro:')
    label_leitor.pack(pady=(15, 0))
    
    Lista_livro = ctk.CTkOptionMenu(emp, values=opcoes_livros ,width=300)
    Lista_livro.set("Selecione")
    Lista_livro.pack(pady=5)

    label_entrega = ctk.CTkLabel(emp, text='Data de entrega do Livro')
    label_entrega.pack(pady=(0, 0))
    campo_entrega = ctk.CTkEntry(emp, placeholder_text='Digite no formato Dia/Mês/Ano',width=200)
    campo_entrega.insert(0,data_de_emprestimo.strftime("%d/%m/%y"))
    campo_entrega.pack(pady=0)

    label_dev = ctk.CTkLabel(emp, text='Devolução dia')
    label_dev.pack(pady=(0, 0))
    campo_dev = ctk.CTkEntry(emp, placeholder_text='Digite no formato Dia/Mês/Ano',width=200)
    campo_dev.insert(0,Data_devolução.strftime("%d/%m/%y"))
    campo_dev.pack(pady=0)

    def ao_fechar():
        Janela_filho.deiconify()  
        emp.destroy()
    emp.protocol("WM_DELETE_WINDOW", ao_fechar)

    botao = ctk.CTkButton(emp, text="cadastrar")
    botao.pack(pady=5)

    emp.mainloop()



