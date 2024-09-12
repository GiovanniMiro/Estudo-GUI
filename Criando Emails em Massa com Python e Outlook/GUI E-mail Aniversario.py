import pandas as pd
from tkinter import *
from tkinter import messagebox, Entry, Label
from tkinter import ttk
from datetime import date
import numpy as np
import gdown
import win32com.client as win32

# -------------------------------------------------------------------------------

root = Tk()
#root.geometry("750x350")
root.title("Email Aniversário")

outlook = win32.Dispatch("outlook.application")

stilo = ttk.Style()
stilo.theme_use("classic")
stilo.configure(".", font=("Arial 12"), rowheight=30)

treeviewDados = ttk.Treeview(root, columns=(1, 2, 3), show="headings")

treeviewDados.column("1", anchor=CENTER)
treeviewDados.heading("1", text="Nome")

treeviewDados.column("2", anchor=CENTER)
treeviewDados.heading("2", text="Nascimento")

treeviewDados.column("3", anchor=CENTER)
treeviewDados.heading("3", text="Email")

treeviewDados.grid(row=2, column=0, columnspan=8, sticky="NSEW")

# --------------------------------------------------------------------------------

arquivo = gdown.download("https://drive.google.com/uc?id=1Awmy3Dpn-tspvkQ_66wxVVXwZ8SEPOLA")

arquivoAniversario = pd.read_excel(arquivo)

#Convertendo a coluna nascimento em texto
arquivoAniversario["Nascimento"] = arquivoAniversario["Nascimento"].astype(str)

#Criando a coluna Ano
arquivoAniversario["Ano"] = arquivoAniversario["Nascimento"].str[:4]

#Criando a coluna Mês
arquivoAniversario["Mes"] = arquivoAniversario["Nascimento"].str[5:7]

#Criando a coluna Dia
arquivoAniversario["Dia"] = arquivoAniversario["Nascimento"].str[-2:]

#Cria uma coluna com a data atual
arquivoAniversario["Data Atual"] = date.today()

arquivoAniversario["Data Atual"] = arquivoAniversario["Data Atual"].astype(str)

#Criando a coluna Ano Atual
arquivoAniversario["Ano Atual"] = arquivoAniversario["Data Atual"].str[:4]

#Criando a coluna Mês Atual
arquivoAniversario["Mes Atual"] = arquivoAniversario["Data Atual"].str[5:7]

#Criando a coluna Dia Atual
arquivoAniversario["Dia Atual"] = arquivoAniversario["Data Atual"].str[-2:]

#Descobrindo os aniversariantes
arquivoAniversario["Aniversario"] = np.where((arquivoAniversario["Mes"] == arquivoAniversario["Mes Atual"]) &
                                             (arquivoAniversario["Dia"] == arquivoAniversario["Dia Atual"]), "Sim", "")

#loc - localiza e limita por um critério (filtra e deixa somente aqueles que satisfazem a condição)
arquivoAniversario = arquivoAniversario.loc[arquivoAniversario["Aniversario"] != "", ["Nome", "Nascimento", "Email"]]


for linha in range(len(arquivoAniversario)):

    #Populando os itens na Treeview com os dados dos aniversariantes do dia.
    treeviewDados.insert("", "end",
                         values=(str(arquivoAniversario.iloc[linha, 0]),    #NOME
                                 str(arquivoAniversario.iloc[linha, 1]),    #ANIVERSÁRIO
                                 str(arquivoAniversario.iloc[linha, 2])))   #EMAIL

labelNome = Label(text="Nome: ", font="Arial 12").grid(row=0, column = 0, sticky="W")
inserirNome = Entry(font="Arial 12")
inserirNome.grid(row=0, column=1, sticky="W")

labelNascimento = Label(text="Nascimento: ", font="Arial 12").grid(row=0, column = 2, sticky="W")
inserirNascimento = Entry(font="Arial 12")
inserirNascimento.grid(row=0, column=3, sticky="W")

labelEmail = Label(text="Email: ", font="Arial 12").grid(row=0, column = 4, sticky="W")
inserirEmail = Entry(font="Arial 12")
inserirEmail.grid(row=0, column=5, sticky="W")

def deletarItem():

    itens = treeviewDados.selection()

    for item in itens:

        #Deletando o item que foi selecionado
        treeviewDados.delete(item)

    inserirNome.delete(0, "end")
    inserirNascimento.delete(0, "end")
    inserirEmail.delete(0, "end")

    messagebox.showinfo("Alerta!", "Item deletado com sucesso!")
    contarNumeroLinhas()



def addItem():

    if inserirNome.get() == "":
        messagebox.showinfo("Atenção!", "Digite um nome!")

    elif inserirNascimento.get() == "":
        messagebox.showinfo("Atenção!", "Digite uma data de nascimento!")

    elif inserirEmail.get() == "":
        messagebox.showinfo("Atenção!", "Digite um email!")

    else:
        treeviewDados.insert("", "end",
                             values=(str(inserirNome.get()),
                                     str(inserirNascimento.get()),
                                     str(inserirEmail.get())))

        inserirNome.delete(0, "end")
        inserirNascimento.delete(0, "end")
        inserirEmail.delete(0, "end")

        messagebox.showinfo("Atenção!", "Pessoa cadastrada com sucesso!")

        contarNumeroLinhas()

def alterarItem():

    if inserirNome.get() == "":
        messagebox.showinfo("Atenção!", "Digite um nome!")

    elif inserirNascimento.get() == "":
        messagebox.showinfo("Atenção!", "Digite uma data de nascimento!")

    elif inserirEmail.get() == "":
        messagebox.showinfo("Atenção!", "Digite um email!")

    else:

        itemSelecionado = treeviewDados.selection()[0]
        treeviewDados.item(itemSelecionado,
                           values=(str(inserirNome.get()),
                                         str(inserirNascimento.get()),
                                         str(inserirEmail.get())))

        inserirNome.delete(0, "end")
        inserirNascimento.delete(0, "end")
        inserirEmail.delete(0, "end")

        messagebox.showinfo("Atenção!", "Item alterado com sucesso!")

def criarEmail():

    for numeroLinha in treeviewDados.get_children():

        #Pego os dados da linha que estiver passando/selecionada naquele momento
        dadosDaLinha = treeviewDados.item(numeroLinha)["values"]

        #Criar um email em branco / Novo email
        emailOutlook = outlook.CreateItem(0)

        email = treeviewDados.item(numeroLinha)["values"][2]
        nome = treeviewDados.item(numeroLinha)["values"][0]

        #split - quebra o nome em colunas de acordo com o critério
        variavelNome = nome.split(" ")[0]

        #<b> - Negrito
        #<font color> - Alterando a cor da letra
        #<a href=""> - Para colocar um hyperlink
        emailOutlook.To = email                                 #Quem recebe
        emailOutlook.Subject = f"Feliz Aniversário, {nome}"  #Título
        emailOutlook.HTMLBody = f"""                 
         <p> Parabéns, <b>{variavelNome}</b>!</p>
         <p> <font color="green">Esse é um dia especial, aproveite seu dia! </font></p>
         <p> <a href="https://www.google.com/"> Clique aqui para acessar seu presente!</a></p>
         <p> Atenciosamente. </p>
         <p><img src="D:\\TKinter\\Criando Emails em Massa com Python e Outlook\\assinatura_email.jpg">.</p>
         """

        # save - Salvar como rascunho / draft
        emailOutlook.save()

    messagebox.showinfo("Alerta!", "Emails criados com sucesso!")

labelNumeroLinhas = Label(text="Linhas: ", font="Arial 20")
labelNumeroLinhas.grid(row=4, column=0, columnspan=8, sticky="W")

def contarNumeroLinhas(item=""):

    numero = 0
    linhas = treeviewDados.get_children(item)

    for linha in linhas:
        numero += 1

    labelNumeroLinhas.config(text="Aniversariantes: " + str(numero))

def passaDadosParaEntry(Event):

    item = treeviewDados.selection()

    for linha in item:

        inserirNome.delete(0,END)
        inserirNascimento.delete(0, END)
        inserirEmail.delete(0, END)

        #Passando os itens da treeview para os campos digitaveis
        inserirNome.insert(0, treeviewDados.item(linha, "values")[0])
        inserirNascimento.insert(0, treeviewDados.item(linha, "values")[1])
        inserirEmail.insert(0, treeviewDados.item(linha, "values")[2])

botaoDeletar = Button(text="Deletar", font="Arial 15",
                      command=deletarItem)
botaoDeletar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

botaoAdicionar = Button(text="Adicionar", font="Arial 15",
                      command=addItem)
botaoAdicionar.grid(row=1, column=2, columnspan=2, sticky="NSEW")

botaoAlterar = Button(text="Alterar", font="Arial 15",
                      command=alterarItem)
botaoAlterar.grid(row=1, column=4, columnspan=2, sticky="NSEW")

botaoEmail = Button(text="Criar Email", font="Arial 15",
                      command=criarEmail)
botaoEmail.grid(row=1, column=6, columnspan=2, sticky="NSEW")

contarNumeroLinhas()

#Programa o evento de duplo clique para chamar a função que passa os dados para o entry.
treeviewDados.bind("<Double-1>", passaDadosParaEntry)

root.mainloop()