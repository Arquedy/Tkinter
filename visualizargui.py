from tkinter import *

class Visualizar:
    def __init__(self):
        self.windows3 = Tk()
        self.frame6 = Frame(self.windows3)
        self.label7 = Label(self.frame6, text = 'Nao sera possivel alterar o nome, tao pouco o CNPJ')

        self.frame7 = Frame(self.windows3)
        self.labelURL = Label(self.frame7, text = 'Qual o novo URL: ')
        self.entradaURL = Entry(self.frame7, width = 25)

        self.frame8 = Frame(self.windows3)
        self.labelTEL = Label(self.frame8, text = 'Qual o novo telefone: ')
        self.entradaTEL = Entry(self.frame8, width = 25)

        self.frame9 = Frame(self.windows3)
        self.labelE = Label(self.frame9, text = 'Qual o novo e-mail: ')
        self.entradaE = Entry(self.frame9, width = 25)

        self.label7.pack(side = 'top')
        self.labelURL.pack(side = 'left')
        self.entradaURL.pack(side = 'left')
        self.labelTEL.pack(side = 'left')
        self.entradaTEL.pack(side = 'left')
        self.labelE.pack(side = 'left')
        self.entradaE.pack(side = 'left')

        self.frame10 = Frame(self.windows3)
        self.botao = Button(self.frame10, text = 'Alterar', command = self.alterar)
        self.sair = Button(self.frame10, text = 'Sair', command = self.feche)

        self.botao.pack(side = 'left')
        self.sair.pack(side = 'left')

        self.frame11 = Frame(self.windows3)
        self.labelD = StringVar
        self.labelText = Label(self.frame11, textvariable = self.labelD)

        self.labelText.pack(side = 'left')

        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.frame9.pack()
        self.frame10.pack()
        self.frame11.pack()


        mainloop()

    def alterar(self):
        pass

    def feche():
        pass

minha = Visualizar()
