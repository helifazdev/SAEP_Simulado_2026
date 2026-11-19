#importação da biblioteca que cria a janela
import customtkinter as ctk
from tkinter import messagebox
from sistema.inicial import exibir_inicial
from sistema.conexao import autenticar_usuario

def exibir_login():#FUNÇÃO DE EXIBIR O LOGIN
    app = ctk.CTk()#Apelido da abertura de janela CTK(app)
    app.title('Login do usuario')#Título da janela
    app.geometry('300x300')#Tamanho da janela
    ctk.set_appearance_mode('Dark') #"System", "Dark" ou "Light"

    def validacao_login(event=None):
        usuario = campo_usuario.get().strip()
        senha = campo_senha.get().strip()

        autenticar = autenticar_usuario(usuario, senha)
        if autenticar:
            app.destroy()
            exibir_inicial()
        else:
            messagebox.showerror("Erro de autenticação","Senha ou usuario estão incorretos!")

    #Label e campo do usuario
    label_usuario = ctk.CTkLabel(app, text='USUARIO')
    label_usuario.pack(pady=(30, 0))
    campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu login')
    campo_usuario.pack(pady=5)

    #Label e campo do senha
    label_senha = ctk.CTkLabel(app, text='SENHA')
    label_senha.pack(pady=(10, 0))
    campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
    campo_senha.pack(pady=5)

    #Botão de entrar
    botao = ctk.CTkButton(app, text="Entrar", command=validacao_login)
    botao.pack(pady=5)

    #mensagem de resultado
    Resultado = ctk.CTkLabel(app,text='')
    Resultado.pack(pady=10)

    app.bind("<Return>", validacao_login)

    app.mainloop()

