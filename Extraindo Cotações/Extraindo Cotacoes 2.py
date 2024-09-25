from webbrowser import Chrome
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#---------------------------------------------------------------------------------------
#Botão para pesquisar o valor da moeda selecionada
def pesquisarItem():

    from select import select
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    import pyautogui as tempoPausaComputador
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.select import Select

    # Service - verifica a versão do Chrome e informa ao Selenium para que o
    # ChromeDriverManager baixe o arquivo correspondente.
    servico = Service(ChromeDriverManager().install())
    meuNavegador = webdriver.Chrome(service=servico)

    #Abre o Google
    meuNavegador.get("https://www.google.com/")

    # Aguarda 3s para dar tempo do computador processar as informações
    tempoPausaComputador.sleep(3)

    # Procurando pelo elemento NAME e quanto encontrar vai escrever Dolar hoje
    meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")

    tempoPausaComputador.sleep(2)

    # Faz a busca pelo valor que está digitado
    meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

    tempoPausaComputador.sleep(4)

    valorDolarGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

    tempoPausaComputador.sleep(2)

    # zuzy3c l84FKc
    todasMoedas = Select(meuNavegador.find_element(By.CLASS_NAME, "l84FKc"))

    linha = 0

    for posicaoItem in todasMoedas.options:

        #Verifica que a opção ou texto da moeda é igual a moeda que está na combobox
        if posicaoItem.text == str(moedaSelecionada.get()):

            tempoPausaComputador.sleep(2)

            #zuzy3c l84FKc
            pegaDropdown = meuNavegador.find_element(By.CLASS_NAME, "l84FKc")

            tempoPausaComputador.sleep(2)

            # Pego todas as informações
            itemSelecionado = Select(pegaDropdown)

            tempoPausaComputador.sleep(3)

            # Seleciono no Dropdown a posição que o Euro está
            itemSelecionado.select_by_index(linha)

            # Interrompo o laço for assim que encontrar o Euro
            break

        linha = linha + 1

    tempoPausaComputador.sleep(5)

    valorDolarGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

    tempoPausaComputador.sleep(1)

    valorMoeda.config(text=str(moedaSelecionada.get()) + ":" + valorDolarGoogle + "\n\n")
#---------------------------------------------------------------------------------------
root = Tk()
root.title("Cotação")

Label(root, text="Moeda: ", font="Arial 20").grid(row=0, column=0)

moedaSelecionada = ttk.Combobox(root, font="Arial 20")
moedaSelecionada["values"] = ('Afegane afegão',
                                'Ariary malgaxe',
                                'Baht tailandês',
                                'Balboa panamenho',
                                'Birr etíope',
                                'Boliviano da Bolívia',
                                'Bolívar soberano',
                                'Cedi ganês',
                                'Colom salvadorenho',
                                'Colón costarriquenho',
                                'Coroa dinamarquesa',
                                'Coroa islandesa',
                                'Coroa norueguesa',
                                'Coroa sueca',
                                'Coroa tcheca',
                                'Córdoba nicaraguense',
                                'Dalasi gambiano',
                                'Dinar argelino',
                                'Dinar bareinita',
                                'Dinar iraquiano',
                                'Dinar jordaniano',
                                'Dinar kuwaitiano',
                                'Dinar líbio',
                                'Dinar macedônio',
                                'Dinar sérvio',
                                'Dinar tunisiano',
                                'Direitos especiais de saque',
                                'Dirham dos Emirados Árabes Unidos',
                                'Dirham marroquino',
                                'Dong vietnamita',
                                'Dram armênio',
                                'Dólar Liberiano',
                                'Dólar americano',
                                'Dólar australiano',
                                'Dólar bahamense',
                                'Dólar barbadense',
                                'Dólar belizenho',
                                'Dólar bermudense',
                                'Dólar bruneano',
                                'Dólar canadense',
                                'Dólar das Ilhas Cayman',
                                'Dólar das Ilhas Salomão',
                                'Dólar de Hong Kong',
                                'Dólar de Trinidad e Tobago',
                                'Dólar do Caribe Oriental',
                                'Dólar fijiano',
                                'Dólar guianense',
                                'Dólar jamaicano',
                                'Dólar namibiano',
                                'Dólar neozelandês',
                                'Dólar singapuriano',
                                'Dólar surinamês',
                                'Escudo cabo-verdiano',
                                'Euro',
                                'Factom',
                                'Florim arubano',
                                'Florim das Antilhas Holandesas',
                                'Florim húngaro',
                                'Franco CFA Central',
                                'Franco CFA ocidental',
                                'Franco CFP',
                                'Franco burundiano',
                                'Franco comoriano',
                                'Franco congolês',
                                'Franco do Djibouti',
                                'Franco guineano',
                                'Franco ruandês',
                                'Franco suíço',
                                'Gourde haitiano',
                                'Guarani paraguaio',
                                'Hryvnia ucraniano',
                                'Iene japonês',
                                'Kina papuásia',
                                'Kip laosiano',
                                'Kwacha malauiana',
                                'Kwacha zambiano',
                                'Kwanza angolano',
                                'Lari georgiano',
                                'Lek albanês',
                                'Lempira hondurenha',
                                'Leone',
                                'Leu moldávio',
                                'Leu romeno',
                                'Lev búlgaro',
                                'Libra Sudanesa',
                                'Libra de Santa Helena',
                                'Libra egípcia',
                                'Libra esterlina',
                                'Libra libanesa',
                                'Lilangeni suazi',
                                'Lira turca',
                                'Loti lesotiano',
                                'Manat azeri',
                                'Manat turcomano',
                                'Marco conversível da Bósnia e Herzegovina',
                                'Metical moçambicano',
                                'Naira nigeriana',
                                'Ngultrum butanês',
                                'Novo dólar taiwanês',
                                'Novo shekel israelense',
                                'Novo sol peruano',
                                'Ouguiya mauritana',
                                'Pataca',
                                'Paʻanga tonganesa',
                                'Peso argentino',
                                'Peso chileno',
                                'Peso colombiano',
                                'Peso cubano',
                                'Peso dominicano',
                                'Peso filipino',
                                'Peso mexicano',
                                'Peso uruguaio',
                                'Pula botsuanesa',
                                'Quetzal guatemalteco',
                                'Quiate',
                                'Rand sul-africano',
                                'Real brasileiro',
                                'Rial catariano',
                                'Rial iemenita',
                                'Rial iraniano',
                                'Rial omanense',
                                'Riel',
                                'Ringgit malaio',
                                'Riyal saudita',
                                'Rublo bielorrusso',
                                'Rublo russo',
                                'Rupia Mauriciana',
                                'Rupia cingalesa',
                                'Rupia das Seychelles',
                                'Rupia indiana',
                                'Rupia indonésia',
                                'Rupia maldívia',
                                'Rupia nepalesa',
                                'Rúpia Paquistanesa',
                                'Som quirguiz',
                                'Som uzbeque',
                                'Somoni',
                                'Taka bengali',
                                'Tenge cazaque',
                                'Unidades de Fomento chilenas',
                                'Won sul-coreano',
                                'Xelim Ugandês',
                                'Xelim queniano',
                                'Xelim somali',
                                'Xelim tanzaniano',
                                'Yuan chinês',
                                'Yuan chinês (offshore)',
                                'Zloty polonês',)

moedaSelecionada.grid(row=0, column=1)

#Selecionando o primeiro item como o padrão
moedaSelecionada.current(0)

botaoPesquisar = Button(text="Pesquisar", font="Arial 20", command=pesquisarItem)
botaoPesquisar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

valorMoeda = Label(root, text="Valor: 0", font="Arial 20")
valorMoeda.grid(row=2, column=0, columnspan=2, sticky="W")
#----------------------------------------------------------------------------------------

root.mainloop()