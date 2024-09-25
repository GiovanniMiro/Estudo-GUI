#import openai
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from groq import Groq

#------------------------------------------------------------------------------------------
client = Groq(api_key="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")


#-------------------------------------------------------------------------------------------

def responder():

    print("Respondendo...")

    #Pega a pergunta do usuário
    pergunta = entrada.get()

    resposta = client.chat.completions.create(
      model="llama3-8b-8192",
      messages=[
        {"role": "user", "content": pergunta}
      ],
      max_tokens=1000,  # Num max de palavras
      temperature=0.7,  # Criatividade
      n=1  # Num de respostas
    )

    respostas.append("Pergunta: " + pergunta)
    respostas.append("Resposta: " + resposta.choices[0].message.content)

    #Adiciona a pergunta na lista lateral
    lista_lateral.insert(END, pergunta)

    #Limpa o conteúdo onde exibe a pergunta e a resposta.
    exibirPergResp.delete(0.0, END)

    for linha in respostas:

      exibirPergResp.insert(END, linha + "\n\n")

    entrada.delete(0, END)

root = Tk()
root.title("Projeto ChatGPT")
root.configure(bg='#17182b')

respostas = []

lista_lateral = Listbox(root, bg="#17182b", fg="#bfc1c2")
lista_lateral.grid(row=0, column=1, rowspan=4, padx=10, pady=10, sticky="NSEW")

exibirPergResp = Text(root, height=5, width=30, bg="#17182b", fg="#bfc1c2")
exibirPergResp.grid(row=0, column=0, pady=10, sticky="NSEW")

labelPergunta = Label(text="Pergunta", font="Arial 15 bold", bg="#17182b", fg="#bfc1c2")
labelPergunta.grid(row=1, column=0, pady=10, sticky="W")

entrada = Entry(root, bg="#17182b", fg="#bfc1c2", font="Arial 20 bold")
entrada.grid(row=2, column=0, pady=10, sticky="NSEW")

botao = Button(root, text="Perguntar", font="Arial 15 bold", command=responder)
botao.grid(row=3, column=0, pady=10, sticky="NSEW")

#Configura a largura para ajustar automaticamente com a tela
root.columnconfigure(0, weight=1)

#Configura onde a linha da janela começa
root.rowconfigure(0, weight=1)

#Maximiza a janela
root.state("zoomed")
root.mainloop()