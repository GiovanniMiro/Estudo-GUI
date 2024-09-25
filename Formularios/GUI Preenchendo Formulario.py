from tkinter.ttk import Style, Treeview
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as tempoEspera


#Abre o arquivo excel
dataset = pd.read_excel("DadosFormulario.xlsx")

root = Tk()
root.title("Preencher Formulário")

stilo = ttk.Style()
stilo.theme_use("alt")
stilo.configure(".", font="Arial 13", rowheight=40)

treeviewDados = Treeview(root, columns=(1, 2, 3, 4, 5), show="headings")
#Centralizar coluna
treeviewDados.column("1", anchor=CENTER)
#Nomear coluna
treeviewDados.heading("1", text="Nome")

treeviewDados.column("2", anchor=CENTER, width=300)
treeviewDados.heading("2", text="Email")

treeviewDados.column("3", anchor=CENTER)
treeviewDados.heading("3", text="Sexo")

treeviewDados.column("4", anchor=CENTER)
treeviewDados.heading("4", text="Estado")

treeviewDados.column("5", anchor=CENTER)
treeviewDados.heading("5", text="Cor")

treeviewDados.grid(row=2, column=0, columnspan=10, sticky="NSEW")

for linha in range(len(dataset)):

    treeviewDados.insert("","end",
                         values=(str(dataset.iloc[linha, 0]),
                                 str(dataset.iloc[linha, 1]),
                                 str(dataset.iloc[linha, 2]),
                                 str(dataset.iloc[linha, 3]),
                                 str(dataset.iloc[linha, 4])))
#------------------------------------------------------------------------------

def preencher_form_massa():

    # Passo linha por linha na treeview
    for child in treeviewDados.get_children():
        # Pego todo o texto da linha que estiver passando da treeview
        linha = treeviewDados.item(child)["values"]

        colunaNome = linha[0]
        colunaEmail = linha[1]
        colunaSexo = linha[2]
        colunaEstado = linha[3]
        colunaCor = linha[4]


        preencher_form(colunaNome, colunaEmail, colunaSexo, colunaEstado, colunaCor)
        tempoEspera.sleep(1)


def preencher_form(nome, email, sexo, estado, cor):

    if nome == "":

        messagebox.showinfo("Atenção!", "Digite um nome.")

    elif email == "":

        messagebox.showinfo("Atenção!", "Digite um email.")

    elif sexo == "":

         messagebox.showinfo("Atenção!", "Digite um sexo.")

    elif estado == "":

        messagebox.showinfo("Atenção!", "Digite um estado.")

    elif cor == "":

        messagebox.showinfo("Atenção!", "Digite uma cor.")

    else:

        # Service - verifica a versao do Chrome e informa ao selenium
        # para que o ChromeDriverManager baixe o seu arquivo
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        navegador.get("https://www.surveymonkey.com/r/79WHF9G")
        tempoEspera.sleep(1)

        #Preencher o nome
        navegador.find_element(By.ID,"112904979").send_keys(nome)
        tempoEspera.sleep(1)

        #Preencher o email
        navegador.find_element(By.ID,"112904987").send_keys(email)
        tempoEspera.sleep(1)

        #Selecionar sexo
        if sexo == "Masculino":
            #Clica na opção do sexo masculino
            navegador.find_element(By.ID,"112905004_855492046_label").click()
        else:
            #Clina na opção do sexo feminino
            navegador.find_element(By.ID,"112905004_855492047_label").click()

        tempoEspera.sleep(2)

        #Selecionar estado no Dropdown
        #Select() é usada para interagir com elementos HTML, que são menus suspensos
        pegaDropdown = Select(navegador.find_element(By.ID,"112905103"))

        linha = 0

        for itemNoDropdown in pegaDropdown.options:

            if itemNoDropdown.text == str(estado):

                tempoEspera.sleep(1)

                #Pego a lista com os numeros até a última posição
                itemSelecionado = Select(navegador.find_element(By.ID,"112905103"))
                tempoEspera.sleep(1)

                #Seleciono o item de acordo com o número que tem na variável linha (posição no dropdown)
                itemSelecionado.select_by_index(linha)

                break

            linha += 1

        tempoEspera.sleep(1)

        #Preencher cor
        navegador.find_element(By.ID,"112905214").send_keys(cor)
        tempoEspera.sleep(1)

        navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()
        tempoEspera.sleep(1)

#-----------------------------------------------------------------------------------------------------------
def add_item():

    if inserirNome.get() == "":

        messagebox.showinfo("Atenção!", "Digite um nome.")

    elif inserirEmail.get() == "":

        messagebox.showinfo("Atenção!", "Digite um email.")

    elif inserirSexo.get() == "":

         messagebox.showinfo("Atenção!", "Digite um sexo.")

    elif inserirEstado.get() == "":

        messagebox.showinfo("Atenção!", "Digite um estado.")

    elif inserirCor.get() == "":

        messagebox.showinfo("Atenção!", "Digite uma cor.")

    else:

        treeviewDados.insert("", "end",
                             values = (str(inserirNome.get()),
                                       str(inserirEmail.get()),
                                       str(inserirSexo.get()),
                                       str(inserirEstado.get()),
                                       str(inserirCor.get())))

        messagebox.showinfo("Mensagem.", "Dados adicionados com sucesso!")

def alterar_item():

    if inserirNome.get() == "":

        messagebox.showinfo("Atenção!", "Digite um nome.")

    elif inserirEmail.get() == "":

        messagebox.showinfo("Atenção!", "Digite um email.")

    elif inserirSexo.get() == "":

         messagebox.showinfo("Atenção!", "Digite um sexo.")

    elif inserirEstado.get() == "":

        messagebox.showinfo("Atenção!", "Digite um estado.")

    elif inserirCor.get() == "":

        messagebox.showinfo("Atenção!", "Digite uma cor.")

    else:

        itemSelecionado = treeviewDados.selection()[0]

        treeviewDados.item(itemSelecionado,
                           values = (str(inserirNome.get()),
                                       str(inserirEmail.get()),
                                       str(inserirSexo.get()),
                                       str(inserirEstado.get()),
                                       str(inserirCor.get())))

        messagebox.showinfo("Mensagem.", "Dados alterados com sucesso!")

        inserirNome.delete(0, "end")
        inserirEmail.delete(0, "end")
        inserirSexo.delete(0, "end")
        inserirEstado.delete(0, "end")
        inserirCor.delete(0, "end")

def dados_para_entries(Event):

        item = treeviewDados.selection()

        for i in item:

            inserirNome.delete(0, "end")
            inserirEmail.delete(0, "end")
            inserirSexo.delete(0, "end")
            inserirEstado.delete(0, "end")
            inserirCor.delete(0, "end")

            inserirNome.insert(0, treeviewDados.item(i, "values")[0])
            inserirEmail.insert(0, treeviewDados.item(i, "values")[1])
            inserirSexo.insert(0, treeviewDados.item(i, "values")[2])
            inserirEstado.insert(0, treeviewDados.item(i, "values")[3])
            inserirCor.insert(0, treeviewDados.item(i, "values")[4])

def excluir_item():

    itensSelecionado = treeviewDados.selection()

    for itemSelecionado in itensSelecionado:

        treeviewDados.delete(itemSelecionado)

    messagebox.showinfo("Atenção!", "Item deletado com sucesso!")
#-----------------------------------------------------------------------------------------------------------
labelNome = Label(text="Nome: ", font="Arial 12")
labelNome.grid(row=0, column=0, sticky="W", pady=5)
inserirNome = Entry(font="Arial 12")
inserirNome.grid(row=0, column=1, sticky="W", pady=5)

labelEmail = Label(text="Email: ", font="Arial 12")
labelEmail.grid(row=0, column=2, sticky="W", pady=5)
inserirEmail = Entry(font="Arial 12")
inserirEmail.grid(row=0, column=3, sticky="W", pady=5)

labelSexo = Label(text="Sexo: ", font="Arial 12")
labelSexo.grid(row=0, column=4, sticky="W", pady=5)
inserirSexo = Entry(font="Arial 12")
inserirSexo.grid(row=0, column=5, sticky="W", pady=5)

labelEstado = Label(text="Estado: ", font="Arial 12")
labelEstado.grid(row=0, column=6, sticky="W", pady=5)
inserirEstado = Entry(font="Arial 12")
inserirEstado.grid(row=0, column=7, sticky="W", pady=5)

labelCor = Label(text="Cor: ", font="Arial 12")
labelCor.grid(row=0, column=8, sticky="W", pady=5)
inserirCor = Entry(font="Arial 12")
inserirCor.grid(row=0, column=9, sticky="W", pady=5)

botaoPreencherMassa = Button(text="Preencher em Massa", font="Arial 20", command=preencher_form_massa)
botaoPreencherMassa.grid(row=1, column=0, columnspan=2, sticky="NSEW")

botaoAdd = Button(text="Adicionar", font="Arial 20", command=add_item)
botaoAdd.grid(row=1, column=2, columnspan=2, sticky="NSEW")

botaoAlterar = Button(text="Alterar", font="Arial 20", command=alterar_item)
botaoAlterar.grid(row=1, column=4, columnspan=2, sticky="NSEW")

botaoExcluir = Button(text="Excluir", font="Arial 20", command=excluir_item)
botaoExcluir.grid(row=1, column=6, columnspan=2, sticky="NSEW")

botaoPreencher = Button(text="Preencher", font="Arial 20", command= lambda: preencher_form(inserirNome.get(), inserirEmail.get(), inserirSexo.get(),
                                                                                  inserirEstado.get(), inserirCor.get()))
botaoPreencher.grid(row=1, column=8, columnspan=2, sticky="NSEW")

treeviewDados.bind("<Double-1>", dados_para_entries)

root.mainloop()
