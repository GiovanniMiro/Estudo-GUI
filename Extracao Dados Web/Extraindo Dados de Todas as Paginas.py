from selenium import webdriver as opcoesSelenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

#Configura o arquivo do Chromedriver para preparar o Chrome
servico = Service(ChromeDriverManager().install())
navegador = opcoesSelenium.Chrome(service=servico)

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

            print("Coluna 1: " + texto2[0])
            print("Coluna 2: " + texto2[1])
            print("Coluna 3: " + texto2[2])

    i += 1

    tempoEspera.sleep(2)

    #Procura pelo XPATH do botão "Next" e clica
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    tempoEspera.sleep(2)