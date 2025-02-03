from  tkinter import*

def funcClicar():
    print("Botão precionado")

    JanelaPrincipal = Tk()
    texto = Label(master = JanelaPrincipal, text="Minha janela exibida")
    texto.pack()

    pic = PhotoImage(file="logo_disqui3.png")
    logo = Label(master=JanelaPrincipal, image=pic)
    logo.pack()
    botao = Button(master=JanelaPrincipal, text="Clique", command=funcClicar)
    botao.pack()
    #texto.place(x = 50, y = 200)

    JanelaPrincipal.mainloop()

if __name__ == '__main__':
    funcClicar()