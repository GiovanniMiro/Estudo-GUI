from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x350')
root.title('Calculadora')

def enviarNumPara(char):
    global calculoOperacoes
    #calculoOperacoes = calculoOperacoes + str(char)
    calculoOperacoes += str(char) #Com o char que só permite 1 item, vou adicionando mais um elemento para a operação.
    textoDeEntrada.set(calculoOperacoes) #Estamos colocando todo o texto na variável que está lincado com o campo do Entry

def deletarNum():
    global calculoOperacoes

    textoSemUltimoDigito = calculoOperacoes[:-1] #Pego todo o texto que está no Entry e excluo apenas o último dígito
    calculoOperacoes = textoSemUltimoDigito #Colocando na variável o texto da operação sem o último dígito.
    textoDeEntrada.set(calculoOperacoes)  # Estamos colocando todo o texto na variável que está lincado com o campo do Entry

def deletarTudo():
    global calculoOperacoes

    calculoOperacoes = '' #Limpando o texto.
    textoDeEntrada.set(calculoOperacoes)  # Estamos colocando todo o texto na variável que está lincado com o campo do Entry

def funcaoIgual():
    global calculoOperacoes

    #eval - Avalia se é um cálculo válido e efetua o cálculo
    resultadoCalculo = str(eval(calculoOperacoes))
    textoDeEntrada.set(resultadoCalculo)

    #Mudo a variável que tinha a operação e coloco apenas o resultado do cálculo na variável
    calculoOperacoes = resultadoCalculo

calculoOperacoes = ''
textoDeEntrada = StringVar()

#Caixa de texto que exibe o resultado e as operações
textoOperacaoResultado = Entry(root, font='Arial 20 bold',
                               textvariable= textoDeEntrada, #Variável
                               border=7, #Borda
                               bg='#BBB', #Cor do fundo
                               fg='black' #Cor da letra
                               ).grid(row=1, columnspan=5, padx= 40, pady= 15, sticky='NSEW') #columnspan é quantas colunas ele vai ocupar

#lambda - Permite enviar vários dados em uma função
#Sticky - Ele estica / preenche as laterais ('NSEW')
#gid - Divide a tela em partes/grades
botaoNum7 = Button(root, text='7', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('7')).grid(row=2, column=0, sticky='NSEW')

botaoNum8 = Button(root, text='8', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('8')).grid(row=2, column=1, sticky='NSEW')

botaoNum9 = Button(root, text='9', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('9')).grid(row=2, column=2, sticky='NSEW')

botaoDel = Button(root, text='DEL', font='Arial 20 bold', border=5, fg= '#000', bg= '#DB701F',
                 command= deletarNum).grid(row=2, column=3, sticky='NSEW')

botaoAC = Button(root, text='AC', font='Arial 20 bold', border=5, fg= '#000', bg= '#DB701F',
                 command= deletarTudo).grid(row=2, column=4, sticky='NSEW')

botaoNum4 = Button(root, text='4', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('4')).grid(row=3, column=0, sticky='NSEW')

botaoNum5 = Button(root, text='5', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('5')).grid(row=3, column=1, sticky='NSEW')

botaoNum6 = Button(root, text='6', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('6')).grid(row=3, column=2, sticky='NSEW')

botaoMultiplicacao = Button(root, text='*', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('*')).grid(row=3, column=3, sticky='NSEW')

botaoDivisao = Button(root, text='/', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('/')).grid(row=3, column=4, sticky='NSEW')

botaoNum1 = Button(root, text='1', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('1')).grid(row=4, column=0, sticky='NSEW')

botaoNum2 = Button(root, text='2', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('2')).grid(row=4, column=1, sticky='NSEW')

botaoNum3 = Button(root, text='3', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('3')).grid(row=4, column=2, sticky='NSEW')

botaoAdicao = Button(root, text='+', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('+')).grid(row=4, column=3, sticky='NSEW')

botaoSubtracao = Button(root, text='-', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('-')).grid(row=4, column=4, sticky='NSEW')

botaoNum0 = Button(root, text='0', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('0')).grid(row=5, column=0, sticky='NSEW')

botaoPonto = Button(root, text='.', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= lambda:enviarNumPara('.')).grid(row=5, column=1, sticky='NSEW')

#columnspan - Colocamos para dize quantas colunas o grid vai ocupar
botaoIgual = Button(root, text='=', font='Arial 20 bold', border=5, fg= 'black', bg= '#BBB',
                 command= funcaoIgual).grid(row=5, column=2, columnspan=3, sticky='NSEW')

root.mainloop()