from tkinter import *
import pymysql
import time
from tkinter import messagebox

class Cadastro:
    def __init__(self):
        self.windows = Tk()
        self.windows.title('Cadastro')
        self.windows.configure(background = 'white')

        self.label = Label(self.windows, text = 'O email nao podera ser o mesmo', bg = 'white')
        self.label1 = Label(self.windows, text = 'Nome', bg = 'white')
        self.label2 = Label(self.windows, text = 'E-mail', bg = 'white')
        self.label3 = Label(self.windows, text = 'Senha', bg = 'white')
        self.label5 = StringVar()
        self.label4 = Label(self.windows, textvariable = self.label5, bg = 'white')

        self.userCadastro = Entry(self.windows, width = 25)
        self.nomeCadastro = Entry(self.windows, width = 25)
        self.senhaCadastro = Entry(self.windows, width = 25)

        self.feito = Button(self.windows, text = 'Cadastrar', bg = 'blue3', command = self.agir)

        self.label.grid(row = 0, columnspan = 2)
        self.label1.grid(row = 1, column = 0)
        self.userCadastro.grid(row = 1, column = 1)
        self.label2.grid(row = 2, column = 0)
        self.nomeCadastro.grid(row = 2, column = 1)
        self.label3.grid(row = 3, column = 0)
        self.senhaCadastro.grid(row = 3, column = 1)
        self.label4.grid(row = 5, column = 1)
        self.feito.grid(row = 4, column = 1, columnspan = 1)

        mainloop()


    def agir(self):
        bd = pymysql.connect(host = 'localhost',
                             user = 'samuel',
                             password = '93254107',
                             db = 'Dados',
                             charset = 'utf8mb4',
                             unix_socket = '/var/run/mysqld/mysqld.sock',
                             cursorclass = pymysql.cursors.DictCursor)

        cursor = bd.cursor()
        sql = """select * from usuarios"""
        cursor.execute(sql)
        resultado2 = cursor.fetchall()
        #bd.close() fecha os dados
        verificacao = True
        user = self.userCadastro.get()
        nome = self.nomeCadastro.get()
        senha = self.senhaCadastro.get()
        for i in resultado2:
             if nome == i['nome']:
                 verificacao = False
        if not verificacao:
                messagebox.showinfo('Espere', 'Usuario ja existente')
        else:
            try:
                sql2 = """insert into usuarios(user, nome, senha, nivel) values ('{}', '{}', '{}', 2)""".format(user, nome, senha)
                cursor.execute(sql2)
                bd.commit()
                time.sleep(5)
                print('Usuario cadastrado')
                cadastrado = 'Usuario cadastrado com sucesso'
                self.label5.set(cadastrado)


            except:
                messagebox.showinfo('ERRO', 'Contate o administrador')


