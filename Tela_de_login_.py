from tkinter import *
janela = Tk()
lb1= Label(janela, text='Login:')
lb2= Label(janela, text='Senha:')
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)

bt = Button(janela, text='Confirmar', command=False, bg='gold')
bt.grid(row=2, column=1, sticky=S)

ed1= Entry(janela)
ed2= Entry(janela)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)

janela.mainloop()