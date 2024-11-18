import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
#dicionário usuários
usuarios = {}

#simbolos
sim = ["@","#","!","$","%*"]

#definindo função mostrar_imagem
def mostrar_imagem(tab, imagem):
    label_for_code = tk.Label(tab, image=imagem)
    label_for_code.pack()
        
#Função que o botão executa
def cadastro() :
    nome = dado_nome.get().title().strip()
    cpf = dado_cpf.get().strip()
    senha = dado_senha.get().strip()
    confirma_senha = dado_confirma_senha.get().strip()


    if nome and cpf and senha:
        if cpf in usuarios:
            messagebox.showerror("Erro!","Usuário já cadastrado com este CPF.")
        elif not len(cpf) == 11 or not cpf.isnumeric():
            messagebox.showwarning("Erro", "Por favor, insira um CPF válido.")
            return 
        elif len(senha) <= 4:
            messagebox.showwarning("Erro", "Senha fraca")
            return
        elif senha.isalpha() or senha.isnumeric() or senha.isalnum():
            messagebox.showwarning("Erro", "Sua senha deve conter ao menos uma letra, um número e um símbolo (!@#$%*).")
            return
        elif not confirma_senha == senha:
            messagebox.showwarning("Erro", "Sua senha deve ser igual à confirmação.")
            return
        else:  
            for c in senha:
                if not c.isalpha() and not c.isnumeric():
                    if c in sim: 
                        usuarios[cpf] = {"nome" : nome, "senha" : senha}
                        messagebox.showinfo("Sucesso!", "Usuário cadastrado com sucesso!")

                        #chamando função mostrar_imagem p/ tab2
                        mostrar_imagem(tab2,imagem)

                        tabControl.add(tab2, text ='Login')
                        tabControl.hide(tab1)
                        

                        label_dados= ttk.Label(tab2, text=f"Olá, {nome}. Faça o Login abaixo:", font = ("Arial", 14, "bold"))
                        label_dados.pack(pady=10)

                        tk.Label(tab2, text="CPF:").pack(anchor = "w", padx=5, pady=5)
                        login_cpf = tk.Entry(tab2)
                        login_cpf.pack(anchor = "w",padx=5 )

                        tk.Label(tab2, text="Senha:").pack(anchor = "w", padx=5, pady=5)
                        login_senha = tk.Entry(tab2)
                        login_senha.pack(anchor = "w",padx=5)
                    else:
                        messagebox.showwarning("Erro", "Sua senha deve conter ao menor um síbolo (!@#$%*).")
                        return 
    else:
        messagebox.showwarning("Atenção!","Preencha todos os campos!")


def login():
    cpf = login_cpf.get().strip()
    senha = login_senha.get().strip()

    if not cpf or not senha:
        messagebox.showinfo("Atenção!", "Preencha os dados abaixo.")
        return
    
    if cpf in usuarios and usuarios[cpf]["senha"] == senha:
        nome = usuarios[cpf]["nome"]
        messagebox.showinfo("Bem-vindo!", f"Login realizado com sucesso! Olá, {nome}.")

    else:
        messagebox.showerror("Erro", "CPF ou senha inválidos.")

def login_existente():
    tabControl.add(tab2, text ='Login')
    tabControl.hide(tab1)

def cadastro_nc():
    tabControl.add(tab1, text ='Cadastro')
    tabControl.hide(tab2)

#criando janela no tkinter
janela = tk.Tk("Sistema de Cadastro")
janela.title("Usuário do Sistema")  
janela.geometry("1000x500")

# Criamos um objeto notebook
tabControl = ttk.Notebook(janela)
tabControl.pack(expand=True, fill = "both")

# Criamos 2 frames (guias)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# Adicionamos os frames ao notebook
tabControl.add(tab1, text ='Cadastro')

#chamando função mostrar_imagem p/ tab1
imagem = tk.PhotoImage(file="images/pequena.png")
mostrar_imagem(tab1,imagem)

#texto cadastre-se
tk.Label(tab1, text="Cadastre-se abaixo:" , font = ("Arial", 12, "bold")).pack(padx=5,pady=10)

#nome
tk.Label(tab1, text="Digite seu nome:").pack(anchor = "w", padx=5, pady=5)
dado_nome = tk.Entry(tab1)
dado_nome.pack(anchor = "w",padx=5 )

#cpf
tk.Label(tab1, text="Digite seu CPF:").pack(anchor = "w", padx=5, pady=5)
dado_cpf = tk.Entry(tab1)
dado_cpf.pack(anchor = "w", padx=5)

#senha
tk.Label(tab1, text="Digite uma senha (Deve conter ABC,123,!@#$%*):").pack(anchor = "w", padx=5, pady=5)
dado_senha = tk.Entry(tab1)
dado_senha.pack(anchor = "w",padx=5)

#Confirme a senha
tk.Label(tab1, text="Confirme sua senha:").pack(anchor = "w", pady=5)
dado_confirma_senha = tk.Entry(tab1)
dado_confirma_senha.pack(anchor = "w",padx=5)

#botão com o comando = função
botão_confirmar = tk.Button(tab1, text="Confirmar", command = cadastro)
botão_confirmar.pack( anchor = "w",padx=5, pady=10)

botão_lexistente = tk.Button(tab1, text="Já possuo login.", command = login_existente)
botão_lexistente.pack( anchor = "center", pady=10)

#chamando função mostrar_imagem p/ tab2
mostrar_imagem(tab2,imagem)

#texto login
tk.Label(tab2, text="Realize o login abaixo:" , font = ("Arial", 12, "bold")).pack(padx=5,pady=10)

#texto de cpf login
tk.Label(tab2, text="CPF:").pack(anchor = "w", padx=5, pady=5)
login_cpf = tk.Entry(tab2)
login_cpf.pack(anchor = "w",padx=5 )

#texto de senha login
tk.Label(tab2, text="Senha:").pack(anchor = "w", padx=5, pady=5)
login_senha = tk.Entry(tab2)
login_senha.pack(anchor = "w",padx=5)

botão_login = tk.Button(tab2, text="Login", command = login)
botão_login.pack( anchor = "w",padx=5, pady=10)

botão_nc = tk.Button(tab2, text="Fazer Cadastro", command = cadastro_nc)
botão_nc.pack( anchor = "center", pady=10)

janela.mainloop()
