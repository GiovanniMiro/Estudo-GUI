from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as tempoEspera


#Service - verifica a versao do Chrome e informa ao selenium
#para que o ChromeDriverManager baixe o seu arquivo
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#Abre o site do formulário
navegador.get("https://www.surveymonkey.com/r/79WHF9G")
tempoEspera.sleep(3)

#Preencher o nome
navegador.find_element(By.ID,"112904979").send_keys("Pessoa")
tempoEspera.sleep(1)

#Preencher o email
navegador.find_element(By.ID,"112904987").send_keys("pessoa@gmail.com")
tempoEspera.sleep(1)

#Selecionar sexo
#Clica na opção do sexo feminino
navegador.find_element(By.ID,"112905004_855492047_label").click()
tempoEspera.sleep(1)

#Selecionar estado no Dropdown
pegaDropdown = navegador.find_element(By.ID,"112905103")
itemSelecionado = Select(pegaDropdown)
itemSelecionado.select_by_index(2)
tempoEspera.sleep(2)

#Preencher cor
navegador.find_element(By.ID,"112905214").send_keys("Azul")
tempoEspera.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()
tempoEspera.sleep(1)