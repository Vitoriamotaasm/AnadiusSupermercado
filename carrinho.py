class Carrinho:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def adicionarProduto(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})
        self.total += produto.preco * quantidade