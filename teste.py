import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

#dicionário usuários
usuarios = {}

#simbolos
sim = ["@","#","!","$","%*"]

#Criando scroll na tab3
def criar_rolavel(tabControl, titulo):

    #Frame externo
    frame_externo = ttk.Frame(tabControl)
    tabControl.add(frame_externo, text=titulo)

    #Canvas
    canvas = tk.Canvas(frame_externo)
    canvas.pack(side="left", fill="both",expand=True)

    #Scrollbar
    scrollbar = ttk.Scrollbar(frame_externo, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right",fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    #Frame interno
    frame_interno = ttk.Frame(canvas)
    canvas.create_window((0,0), window= frame_interno, anchor="nw")

    def ajustar_scroll(evento):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_interno.bind("<Configure>", ajustar_scroll)

    return frame_interno

def adicionar_tab():
    global aba_rolavel_add
    if not aba_rolavel_add:
        tab3 = criar_rolavel(tabControl,"PDI")

        #chamando função mostrar_imagem p/ tab3
        mostrar_imagem(tab3,imagem)

        #texto PDI
        tk.Label(tab3,text=f"Bem vindo ao seu Plano de Desenvolvimento Individual! Preencha os campos abaixo:", font = ("Arial", 12, "bold")).pack(anchor="center", pady=10)
        tk.Label(tab3,text=f"Avalie as competências abaixo de 0 a 5: \n Sendo 0 = Não conheço e 5 = Domino plenamente e consigo ir além \n", font = ("Arial", 10, "")).pack(anchor="center", pady=10)


        criar_opcoes("MatPlotLib", mtl_var,tab3 )
        criar_opcoes("Pandas",pds_var,tab3)
        criar_opcoes("Numpy",numpy_var,tab3)
        criar_opcoes("Tkinter",tk_var,tab3)
        criar_opcoes("Flask",flask_var,tab3)

        botão_pdi = tk.Button(tab3, text="Enviar", command=salvar_pdi,bg="green",fg="white")
        botão_pdi.pack(anchor="center", pady=10)

        botão_limpar = tk.Button(tab3, text="Limpar Campos", command=limpar_campos,bg="red",fg="white")
        botão_limpar.pack(anchor="center", pady=10)

        aba_rolavel_add = True

#definindo função mostrar_imagem
def mostrar_imagem(tab, imagem):
    label_for_code = tk.Label(tab, image=imagem)
    label_for_code.pack(anchor="center")
        
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

                        tabControl.add(tab2, text ='Login')
                        tabControl.hide(tab1)
                        
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

        adicionar_tab()
        tabControl.hide(tab2)

    else:
        messagebox.showerror("Erro", "CPF ou senha inválidos.")

def login_existente():
    tabControl.add(tab2, text ='Login')
    tabControl.hide(tab1)

def cadastro_nc():
    tabControl.add(tab1, text ='Cadastro')
    tabControl.hide(tab2)

def salvar_pdi():
    nome = dado_nome.get().strip()

    resultados = { 
        "MatPlotLib" : mtl_var.get(),
        "Pandas" : pds_var.get(),
        "Numpy" : numpy_var.get(),
        "Tkinter" : tk_var.get(),
        "Flask" : flask_var.get()
    }
    
    #Verificar se todas as perguntas foram preenchidas
    if any(valor == -1 for valor in resultados.values()):
        messagebox.showwarning("Aviso","Por favor, avalie todas as competências.")
        return

    #Salvar dados em um arquivo
    with open("pdi_avaliações_opções.txt", "a") as file:
        file.write(f"Nome: {nome}")
        for habilidade, nota in resultados.itens():
            file.write(f"{habilidade} : {nota}/5\n")
        file.write("-" * 30 + "\n")

    messagebox.showinfo("Sucesso!", "Avaliação salva com sucesso!")
    limpar_campos()

def limpar_campos():
    mtl_var.set(-1)
    pds_var.set(-1)
    numpy_var.set(-1)
    tk_var.set(-1)
    flask_var.set(-1)

def criar_opcoes(titulo, var, tab3):
    frame = tk.Frame(tab3)
    frame.pack(anchor="w", padx=10, pady=5)
    tk.Label(frame, text=titulo).pack(anchor="w")
    
    for i in range(6): 
        tk.Radiobutton(frame, text=str(i), variable= var, value=i).pack(side="left")




#criando janela no tkinter
janela = tk.Tk("Sistema de Cadastro")
janela.title("Usuário do Sistema")  
janela.geometry("1000x500")

# Criamos um objeto notebook
tabControl = ttk.Notebook(janela)
tabControl.pack(expand=True, fill = "both")

# Criamos 3 frames (guias)
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
tk.Label( tab2, text=f"Olá! Realize o login abaixo:" , font = ("Arial", 12, "bold")). pack(padx=5,pady=10)

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

#Variáveis que vão armazenas as avaliações
mtl_var = tk.IntVar(value=-1)
pds_var = tk.IntVar(value=-1)
numpy_var = tk.IntVar(value=-1)
tk_var = tk.IntVar(value=-1)
flask_var = tk.IntVar(value=-1)

aba_rolavel_add = False


janela.mainloop()
