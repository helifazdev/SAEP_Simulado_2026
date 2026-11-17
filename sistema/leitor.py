import customtkinter as ctk

def cadastrar_leitor(Janela_filho):#FUNÇÃO DE CADASTRO DE LIVROS
    cad = ctk.CTkToplevel(Janela_filho)#Apelido da abertura de janela CTK(app)
    cad.title('Cadastro de Leitor')#Título da janela
    cad.geometry('600x400')#Tamanho da janela
    ctk.set_appearance_mode('System') #"System", "Dark" ou "Light"

    label_leitor = ctk.CTkLabel(cad, text='Nome do leitor (*)')
    label_leitor.pack(pady=(0, 0))
    campo_leitor = ctk.CTkEntry(cad, placeholder_text='Digite o nome do leitor')
    campo_leitor.pack(pady=0)

    label_instituicao = ctk.CTkLabel(cad, text='instituição')
    label_instituicao.pack(pady=(0, 0))
    campo_instituicao = ctk.CTkEntry(cad, placeholder_text='Digite a instuição que o leitor é vinculado',width=200)
    campo_instituicao.pack(pady=0)

    label_cpf = ctk.CTkLabel(cad, text='CPF (*)')
    label_cpf.pack(pady=(0, 0))
    campo_cpf = ctk.CTkEntry(cad, placeholder_text='Digite numero do CPF',width=200)
    campo_cpf.pack(pady=0)

    label_email = ctk.CTkLabel(cad, text='E-mail (*)')
    label_email.pack(pady=(0, 0))
    campo_email = ctk.CTkEntry(cad, placeholder_text='Digite o email do leitor')
    campo_email.pack(pady=0)

    label_senha = ctk.CTkLabel(cad, text='SENHA (*)')
    label_senha.pack(pady=(0, 0))
    campo_senha = ctk.CTkEntry(cad, placeholder_text='Peça para o leitor digitar a senha')
    campo_senha.pack(pady=0)

    label_senha_novamente = ctk.CTkLabel(cad, text='Senha novamente (*)')
    label_senha_novamente.pack(pady=(0, 0))
    campo_senha_novamente = ctk.CTkEntry(cad, placeholder_text='Digite a senha novemente',width=200)
    campo_senha_novamente.pack(pady=0)

    #Botão de entrar
    botao = ctk.CTkButton(cad, text="cadastrar Leitor")
    botao.pack(pady=5)

    cad.mainloop()
 
