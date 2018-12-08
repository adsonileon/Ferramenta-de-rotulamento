from tkinter import *
from Gerenciador import *
class Application:
    def __init__(self, master=None):
        self.gerenciador = Gerenciador("amostra.csv")

        self.fonte = ("Verdana", "12")
  
        self.container1 = Frame(master)
        self.container1.pack()
        self.container3 = Frame(master)
        self.container3.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        #self.container5 = Frame(master)
        #self.container5["padx"] = 20
        #self.container5["pady"] = 5
        #self.container5.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.titulo = Text(self.container1, wrap=WORD, width=126)
        self.titulo["font"] = self.fonte
        self.titulo.pack()

        self.atual = Label(self.container3, text="Atual: " + self.getNumAtual() + " |", font=self.fonte)
        self.atual.pack(side=LEFT)
        self.total = Label(self.container3, text="Total: " + self.getTotal(), font=self.fonte)
        self.total.pack(side=LEFT)

        self.imprimePost()

        self.btnF = Button(self.container2, text="Furto", font=self.fonte, width=7)
        self.btnF["command"] = self.setClassF
        self.btnF.pack(side=LEFT)
        
        self.btnRV = Button(self.container2, text="Roubo", font=self.fonte, width=7)
        self.btnRV["command"] = self.setClassR
        self.btnRV.pack(side=LEFT)
      
        self.btnTV = Button(self.container2, text="Tentativa", font=self.fonte, width=10)
        self.btnTV["command"] = self.setClassT
        self.btnTV.pack(side=LEFT)

        self.btnO = Button(self.container2, text="Outros", font=self.fonte, width=7)
        self.btnO["command"] = self.setClassO
        self.btnO.pack(side=LEFT)

        #self.btnL = Button(self.container5, text="Com Localização", font=self.fonte, width=14)
        #self.btnL["command"] = self.setClassL
        #self.btnL.pack(side=LEFT)

        #self.btnSL = Button(self.container5, text="Sem Localização", font=self.fonte, width=14)
        #self.btnSL["command"] = self.setClassSL
        #self.btnSL.pack(side=LEFT)

        self.btnP = Button(self.container2, text="Próximo", font=self.fonte, width=7)
        self.btnP["command"] = self.proximoPost
        self.btnP.pack(side=LEFT)

        self.btnE = Button(self.container4, text="Editar", font=self.fonte, width=7)
        self.btnE["command"] = self.editar
        self.btnE.pack(side=LEFT)

        self.btnA = Button(self.container4, text="Apagar", font=self.fonte, width=7)
        self.btnA["command"] = self.excluir
        self.btnA.pack(side=LEFT)

        self.btnS = Button(self.container4, text="Salvar", font=self.fonte, width=7)
        self.btnS["command"] = self.salvar
        self.btnS.pack(side=LEFT)
  
    def getNumAtual(self):
        return self.gerenciador.getAtual()

    def getTotal(self):
        return self.gerenciador.getTotal()

    def getPost(self):
        return self.gerenciador.getConteudoPost()

    def getLikes(self):
        return self.gerenciador.getLikes()

    def getComentarios(self):
        return self.gerenciador.getComentarios()

    def getData(self):
        return self.gerenciador.getData()

    def getFonte(self):
        return self.gerenciador.getFonte()

    def getClassificacao(self):
        return self.gerenciador.getClassificacao()

    def getClassificacao2(self):
        return self.gerenciador.getClassificacao2()

    def proximoPost(self):
        self.gerenciador.proximoPost()
        self.imprimePost()
        
    def imprimePost(self):
        self.atual["text"] = "Atual: " + self.getNumAtual() + " |"
        self.total["text"] = "Total: " + self.getTotal()
        self.titulo.config(state=NORMAL)
        self.titulo.delete('1.0',END)
        self.titulo.insert(END,"Post:" + self.getPost())
        self.titulo.insert(END,"\nLikes: " + self.getLikes())
        self.titulo.insert(END,"\nComentários: " + self.getComentarios())
        self.titulo.insert(END,"\nData: " + self.getData())
        self.titulo.insert(END, "\nFonte: " + self.getFonte())
        self.titulo.insert(END, "\n\nClassificação: " + self.getClassificacao())
        #self.titulo.insert(END, "\nClassificação 2: " + self.getClassificacao2())
        self.titulo.config(state=DISABLED)

    def setConteudo(self, conteudo):
        self.gerenciador.setConteudo(conteudo)

    def setClassF(self):
        self.gerenciador.setClassificacao("Furto")
        self.imprimePost()

    def setClassR(self):
        self.gerenciador.setClassificacao("Roubo")
        self.imprimePost()

    def setClassT(self):
        self.gerenciador.setClassificacao("Tentativa")
        self.imprimePost()

    def setClassO(self):
        self.gerenciador.setClassificacao("Outros")
        self.imprimePost()

    def setClassL(self):
        self.gerenciador.setClassificacao2("Com localização")
        self.imprimePost()

    def setClassSL(self):
        self.gerenciador.setClassificacao2("Sem Localização")
        self.imprimePost()

    def editar(self):
        self.janela = Toplevel()
        self.cont1 = Frame(self.janela)
        self.cont1.pack()
        self.cont2 = Frame(self.janela)
        self.cont2["padx"] = 20
        self.cont2["pady"] = 5
        self.cont2.pack()
        self.textoEd = Text(self.cont1, wrap=WORD, width=126)
        self.textoEd.insert(END, self.getPost())
        self.textoEd["font"] = self.fonte
        self.textoEd.pack()
        self.btnSED = Button(self.cont1, text="Salvar", font=self.fonte, width=7)
        self.btnSED["command"] = self.atualizar
        self.btnSED.pack()

    def atualizar(self):
        self.setConteudo(self.textoEd.get("1.0", END))
        self.janela.destroy()
        self.imprimePost()

    def excluir(self):
        self.gerenciador.excluir()
        self.imprimePost()

    def salvar(self):
        self.gerenciador.salvar()

root = Tk()
root.attributes()
Application(root)
root.mainloop()
