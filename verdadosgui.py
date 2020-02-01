from tkinter import *

class MinhaGUI:
    def __init__(self):
        self.windows4 = Tk()
        self.windows4.title('Consulta')
        self.frame = Frame(self.windows4)
        self.label = Label(self.frame, text = 'Qual o nome da empresa?')
        self.entrada = Entry(self.frame, width = 25)

        self.label.pack(side = 'left')
        self.entrada.pack(side = 'left')

        self.frame1 = Frame(self.windows4)
        self.label2 = Label(self.frame1, text = 'Qual CNPJ?')
        self.espaco = Label(self.frame1, text = '                        ')
        self.entrada2 = Entry(self.frame1, width = 25)

        self.label2.pack(side = 'left')
        self.espaco.pack(side = 'left')
        self.entrada2.pack(side = 'left')

        self.frame2 = Frame(self.windows4)
        self.botao = Button(self.frame2, text = 'Procurar', command = self.search)
        self.botao_sair = Button(self.frame2, text = 'Sair', command = self.exit)

        self.botao.pack(side = 'left')
        self.botao_sair.pack(side = 'left')

        self.frame3 = Frame(self.windows4)
        self.labelres = StringVar
        self.label3 = Label(self.frame3, textvariable = self.labelres)

        self.label3.pack(side = 'left')

        self.frame.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        mainloop()

    def search(self):
        pass

    def exit(self):
        quit()

minha = MinhaGUI()
