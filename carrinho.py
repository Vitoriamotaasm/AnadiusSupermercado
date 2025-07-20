class Carrinho:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def adicionarProduto(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade