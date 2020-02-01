from tkinter import *
import pymysql
import time
from tkinter import messagebox
from cadastro import Cadastro
class Login:
    def __init__(self):
        self.cadastro = Tk()
        self.cadastro.title('Bem-vindo')
        self.cadastro.configure(background = 'white')

        self.label = Label(self.cadastro, text = 'Faça seu Login', bg = 'white', fg = 'blue')
        self.label1 = Label(self.cadastro, text = 'Seu E-mail', bg = 'white')
        self.label2 = Label(self.cadastro, text = 'Sua senha', bg = 'white')
        self.label3 = Label(self.cadastro, text = 'Ainda não tem conta?', bg = 'white')
        self.labelVar = StringVar()
        self.label4 = Label(self.cadastro, textvariable = self.labelVar, bg = 'white' )

        self.cadastrar = Button(self.cadastro, text = 'Cadastre-se', bg = 'orange3', command = self.cadastre)
        self.login = Button(self.cadastro, text = 'Login', bg = 'green3', command = self.login)

        self.email_entry = Entry(self.cadastro, width = 35)
        self.senha_entry = Entry(self.cadastro, width = 35)

        self.label.grid(row = 0, column = 1, padx = 20, columnspan = 2)
        self.label1.grid(row = 1, column = 1, padx = 20, columnspan = 2)
        self.email_entry.grid(row = 2, column = 1, padx = 20, columnspan = 2)
        self.label2.grid(row = 3, column = 1, padx = 20, columnspan = 2)
        self.senha_entry.grid(row = 4, column = 1, padx = 20, columnspan = 2)
        self.login.grid(row = 5, column = 1, padx = 20, columnspan = 2)
        self.label4.grid(row = 6, column = 1, padx = 20, columnspan = 2)
        self.label3.grid(row = 7, column = 1, stick = 'E')
        self.cadastrar.grid(row = 7, column = 2, stick = 'W')

        mainloop()

    def cadastre(self):
        cad = Cadastro()


    def login(self):
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
        resultado = cursor.fetchall()
        #bd.commit() para inserir cadastrados
        #bd.close() fecha os dados
        login = self.email_entry.get()
        senha = self.senha_entry.get()
        usuarioAtenticado = False
        usuarioMaster = False
        for i in resultado:
            if login == i['nome'] and senha == i['senha']:
                if i['nivel'] == 1:
                    usuarioMaster = True
                elif i['nivel'] == 2:
                    usuarioMaster == False
                usuarioAtenticado = True
                if usuarioAtenticado and usuarioMaster:
                    print('Procurando e identificando usuario')
                    loginShearch = 'Procurando e indentificando usuario'
                    self.labelVar.set(loginShearch)
                    time.sleep(5)
                    print('Usuario root logado, tenha cuidado')
                    loginRight = 'Usuario root logado com sucesso'
                    self.labelVar.set(loginRight)

                elif usuarioAtenticado and not usuarioMaster:
                    print('Usuario comum, opçoes limitadas')
                    loginHost = 'Logado'
                    self.labelVar.set(loginHost)

                break
            else:
                usuarioAtenticado = False
        if not usuarioAtenticado:
            print('Usuario teve um erro')
            erro = 'E-mail ou senha errado'
            self.labelVar.set(erro)
login = Login()
