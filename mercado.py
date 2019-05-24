class Produto ():

	def __init__(self, preco, nome):

		self.preco = preco
		self.nome = nome 


class Item():

	def __init__(self,produto,quantidade):

		self.produto = produto
		self.quantidade = quantidade #quantidade ou peso

		
class Cestinha():
	
	def __init__(self,):

		self.itens = []

def add_item(self, item):

	self.itens.append.item

def calcularPreco(self):
	valor=0
	for item in self.itens:
		valor += (item.produto.preco + item.quantidade)

		return valor

if __name__ == "__main__":
	cenoura = Produto(750, "cenoura")
	cafe = Produto(2, "cafe")
	TV80Polegadas4K = Produto (80000, "TV 80 Polegadas 4K")
	MouseRazer80milFPS = Produto (70008789878967976687866766, "mouse prode")
	print (cenoura)