from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        self.windows = Tk()
        self.frame1 = Frame(self.windows)
        self.label1 = Label(self.frame1, text = 'Aqui surgira um resultado', bg = 'blue')
        self.entrada = Entry(self.frame1, width = 30)
        self.label1.pack(side = 'left')
        self.entrada.pack(side = 'left')

        self.frame2 = Frame(self.windows)
        self.botao = Button(self.frame2, text = 'Resultado', bg = 'red', fg = 'red', command = self.soma)
        self.encerrar = Button(self.frame2, text = 'sair', command = self.quit)
        self.botao.pack(side = 'left')
        self.encerrar.pack(side = 'left')

        self.frame1.pack()
        self.frame2.pack()

        mainloop()

    def soma(self):
        messagebox.showinfo('Janela de teste', 'A soma false é' + self.entrada.get())
    def quit(self):
        pass

minha = MinhaGUI()
