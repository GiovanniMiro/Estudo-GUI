from http.server import executable
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from threading import Thread

def iniciar_selenium():
    from selenium import webdriver as opcoesSelenium
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import pyautogui as tempoEspera

    # Definindo o caminho para o ChromeDriver
    servico = Service("C:\\Users\\giova\\anaconda3\\chromedriver.exe")

    # Configurando as opções do Chrome
    opcoes = Options()
    opcoes.add_argument("--headless")  # Executar o navegador sem abrir a interface gráfica
    opcoes.headless = True

    # Inicializando o navegador com o serviço e as opções
    navegador = opcoesSelenium.Chrome(service=servico, options=opcoes)

    tempoEspera.sleep(1)

    #Abre o site
    navegador.get("https://rpachallengeocr.azurewebsites.net/")

    tempoEspera.sleep(3)

    linha = 1
    i = 1

    while i < 4:
        # Seleciona a tabela através do XPATH
        elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

        linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
        colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

        tempoEspera.sleep(1)

        for linhaAtual in linhas:

            tempoEspera.sleep(1)

            linha += 1

            texto = linhaAtual.text

            if texto[0] != "#":

                #Separamos com o split todas as palavrras em colunas com o critéio de espaço
                texto2 = texto.split(" ")

                #print("Coluna 1: " + texto2[0])
                #print("Coluna 2: " + texto2[1])
                #print("Coluna 3: " + texto2[2])

                #Populando as linhas da treeview
                treeviewDados.insert("", "end",
                                     values=(str(texto2[0]),
                                             str(texto2[1]),
                                             str(texto2[2])))

        i += 1

        tempoEspera.sleep(2)

        #Procura pelo XPATH do botão "Next" e clica
        navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

        tempoEspera.sleep(2)

def exportarParaExcel():
    from openpyxl import load_workbook

    #Abrindo o arquivo do EXCEL
    workbook = load_workbook("Base_Dados.xlsx")

    #Selecionando a sheet / planilha que vai receber os dados
    sheet = workbook["Dados"]

    #Deletando os dados
    sheet.delete_rows(idx=1, amount=30000)

    #Passando linha por linha na treeview e imprimindo no arquivo do EXCEL
    for numeroLinha in treeviewDados.get_children():

        #Pegando os valores da linha corrente da treeview
        textosDaLinha = treeviewDados.item(numeroLinha)["values"]

        #Colocando o texto de cada linha um embaixo do outro na planilha
        sheet.append(textosDaLinha)

        #Salvando o arquivo
        workbook.save(filename="Dados_Extraidos_WEB.xlsx")

    messagebox.showinfo("Atenção", "Dados exportados com sucesso!")

root = Tk()
root.title("Extraindo Dados WEB")

stilo = ttk.Style()
stilo.theme_use("alt")
stilo.configure(".", font="Arial 15", rowheight=40)

treeviewDados = ttk.Treeview(root, columns=(1, 2, 3), show="headings")

treeviewDados.column("1", width=100, anchor=CENTER)
treeviewDados.heading("1", text="ID")

treeviewDados.column("2", width=500, anchor=CENTER)
treeviewDados.heading("2", text="Due Date")

treeviewDados.column("3", width=200, anchor=CENTER)
treeviewDados.heading("3", text="Invoice")

treeviewDados.grid(row=0, column=0, columnspan=8, sticky="NSEW")

#Configura o botão
botaoExportar = Button(text="Exportar", font="Arial 20",
                       command=exportarParaExcel)

botaoExportar.grid(row=1, column=0, columnspan=8, sticky="NSEW")

iniciar_selenium()

root.mainloop()