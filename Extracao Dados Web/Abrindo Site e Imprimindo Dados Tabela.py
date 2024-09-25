from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

#Configura o arquivo do Chromedriver para preparar o Chrome
navegador = opcoesSelenium.Chrome()

#Abre o site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

tempoEspera.sleep(3)

#Seleciona a tabela através do XPATH
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

#linha = 1

for linhaAtual in linhas:

    tempoEspera.sleep(1)

    print(linhaAtual.text)