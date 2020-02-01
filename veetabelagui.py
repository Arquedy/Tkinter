from tkinter import *
import pymysql

class Dados:
    def __init__(self):
        self.windows5 = Tk()
        self.frame1 = Frame(self.windows5)
        self.label = Label(self.frame1, text = 'Essa janela ira mostrar dados de todos os clientes')
        self.label1 = Label(self.frame1, text = 'Se quer somente de um cliente escolha outra opção')

        self.label.pack(side = 'top')
        self.label1.pack(side = 'top')

        self.frame2 = Frame(self.windows5)
        self.label_consulta = StringVar
        self.label2 = Label(self.frame2, textvariable = self.label_consulta)

        self.frame2.pack(side = 'left')

        self.frame3 = Frame(self.windows5)
        self.botao = Button(self.frame3, text = 'Mostrar', command = self.mostrar)
        self.fechar = Button(self.frame3, text = 'Fechar', command = self.fechar)

        self.botao.pack(side = 'left')
        self.fechar.pack(side = 'left')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        mainloop()

    def mostrar(self):


    def fechar(self):
        pass


        mainloop()

minha = Dados()
