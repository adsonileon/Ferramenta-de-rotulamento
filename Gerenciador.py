import csv

class Gerenciador:

    def __init__(self, caminho):
        arquivo = open(caminho, 'r', encoding="utf-8")
        reader = csv.reader(arquivo, delimiter=';')
        self.posts = []
        self.lidos = -1
        i = -1
        for linha in reader:
            if(i!=-1):
                if(linha[6]=="" and self.lidos==-1):
                    self.lidos = i;
                self.posts.append(linha)
            i = i + 1
        self.total = len(self.posts)
        arquivo.close()

    def getTotal(self):
        return str(self.total)

    def getAtual(self):
        return str(self.lidos+1)

    def getConteudoPost(self):
        return self.convert65536(self.posts[self.lidos][0])

    def getLikes(self):
        return self.posts[self.lidos][1]

    def getComentarios(self):
        return self.posts[self.lidos][2]

    def getData(self):
        return self.posts[self.lidos][3]

    def getFonte(self):
        return self.posts[self.lidos][5]

    def getClassificacao(self):
        return self.posts[self.lidos][6]

    def getClassificacao2(self):
    	return self.posts[self.lidos][7]

    def setConteudo(self, conteudo):
        self.posts[self.lidos][0] = conteudo

    def setClassificacao(self, classificacao):
        self.posts[self.lidos][6] = classificacao

    def setClassificacao2(self, classificacao):
    	self.posts[self.lidos][7] = classificacao

    def proximoPost(self):
        if(self.lidos + 1 < len(self.posts)):
            self.lidos = self.lidos + 1
    def excluir(self):
        del self.posts[self.lidos]
        self.total = len(self.posts)
        if(self.lidos == self.total):
            self.lidos = self.lidos - 1

    def salvar(self):
        with open("backup-"+str(self.lidos+1)+".csv", 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Conteudo', 'Likes', 'Comentarios', 'Data', 'Link Comentarios', 'Fonte', 'Classificacao 1', 'Classificacao 2'])
            for linha in self.posts:
                spamwriter.writerow(linha)
        print('Arquivo gerado no diretorio: backup-' + str(self.lidos+1) + ".csv")


    def convert65536(self, s):
        #Converts a string with out-of-range characters in it into a string with codes in it.
        l=list(s);
        i=0;
        while i<len(l):
            o=ord(l[i]);
            if o>65535:
                l[i]="{"+str(o)+"ū}";
            i+=1;
        return "".join(l);








