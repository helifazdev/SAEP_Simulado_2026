#importação da biblioteca que cria a janela
import customtkinter as ctk
from sistema.conexao import cadastrar_livro as importa_no_banco
from tkinter import messagebox

def cadastrar_livro(Janela_filho):#FUNÇÃO DE CADASTRO DE LIVROS
    cad = ctk.CTkToplevel(Janela_filho)#Apelido da abertura de janela CTK(app)
    cad.title('Cadastro de livros')#Título da janela
    cad.geometry('600x500')#Tamanho da janela
    ctk.set_appearance_mode('System') #"System", "Dark" ou "Light"

    label_titulo = ctk.CTkLabel(cad, text='TITULO (*)')
    label_titulo.pack(pady=(0, 0))
    campo_titulo = ctk.CTkEntry(cad, placeholder_text='Digite o título do livro')
    campo_titulo.pack(pady=0)

    label_autor = ctk.CTkLabel(cad, text='AUTOR (*)')
    label_autor.pack(pady=(0, 0))
    campo_autor = ctk.CTkEntry(cad, placeholder_text='Digite nome(s) do(s) autor(es)',width=200)
    campo_autor.pack(pady=0)

    label_editora = ctk.CTkLabel(cad, text='EDITORA (*)')
    label_editora.pack(pady=(0, 0))
    campo_editora = ctk.CTkEntry(cad, placeholder_text='Digite nome da editora')
    campo_editora.pack(pady=0)

    label_isbn = ctk.CTkLabel(cad, text='ISBN (*)')
    label_isbn.pack(pady=(0, 0))
    campo_isbn = ctk.CTkEntry(cad, placeholder_text='Digite o ISBN')
    campo_isbn.pack(pady=0)

    label_ano_public = ctk.CTkLabel(cad, text='Ano de publicação (*)')
    label_ano_public.pack(pady=(0, 0))
    campo_ano_public = ctk.CTkEntry(cad, placeholder_text='Digite no formato AAAA',width=200)
    campo_ano_public.pack(pady=0)

    label_edicao = ctk.CTkLabel(cad, text='EDIÇÃO')
    label_edicao.pack(pady=(0, 0))
    campo_edicao = ctk.CTkEntry(cad, placeholder_text='Digite a edição do livro',width=200)
    campo_edicao.pack(pady=0)

    def salvar():
        tit = campo_titulo.get().strip()
        aut = campo_autor.get().strip()
        edi = campo_editora.get().strip()
        isbn = campo_isbn.get().strip()
        ano = campo_ano_public.get().strip()
        edic = campo_edicao.get().strip()

        if not all([tit,aut,edi,isbn,ano]):
            messagebox.showwarning("Atenção!","Os campos com (*) são obrigatórios, " \
            "preencha todos para continuar")
            return

        sucesso, mensagem = importa_no_banco(tit,aut,edi,isbn,ano,edic)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("ERRO", mensagem)
    
    botao = ctk.CTkButton(cad, text="cadastrar",command=salvar)
    botao.pack(pady=5)

   