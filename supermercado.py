from produto import Produto
from cliente import Cliente
from carrinho import Carrinho

class Supermercado:
    def __init__(self):
        self.produtos = {}
        self.clientes = {}

    def cadastrarProduto(self, nome, preco, estoque):
        self.produtos[nome] = Produto(nome,preco,estoque)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    def buscarProduto(self, nome):
          if nome in self.produtos:
            print(f"Produto '{nome}' ja está cadastrado!.")
            return
          
    def cadastrarCliente(self, nome, cpf):
        self.clientes[nome] = Cliente(nome, cpf)
        print(f"Cliente '{nome}' cadastrado com sucesso!")

    def realizarVenda(self, cliente, carrinho):
        for item in carrinho.itens:
            produto = item['produto']
            quantidade = item['quantidade']

            if produto.estoque >= quantidade:
                produto.estoque -= quantidade
            else:
                print(f"Estoque insuficiente para o produto '{produto.nome}")
        print(f"Venda realizada com sucesso para o cliente '{cliente.nome}'!")
