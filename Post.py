class Post:

	def __init__(self, conteudo, numLikes, numComentarios, data, linkComentario, fonte, classificacao):
		self.conteudo = conteudo
		self.numLikes = numLikes
		self.numComentarios = numComentarios
		self.data = data
		self.linkComentario = linkComentario
		self.fonte = fonte
		self.classificacao = classificacao

	def getConteudo(self):
		return self.conteudo

	def getNumLikes(self):
		return self.numLikes

	def getNumComentarios(self):
		return self.numComentarios

	def getData(self):
		return self.data

	def getLinkComentario(self):
		return self.linkComentario

	def getFonte(self):
		return self.fonte

	def getClassificacao(self):
		return self.classificacao