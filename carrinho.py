class Carrinho:
    def __init__(self):
        self.itens = []
        self.total = 0.0

    def adicionar(self, produto, quantidade):
        if quantidade > produto.estoque:
            print(f"Erro: Estoque insuficiente para o produto '{produto.nome}'.")
            return
        self.itens.append({"produto": produto, "quantidade": quantidade})
        self.total += produto.preco * quantidade
        print(f"{quantidade}x {produto.nome} adicionado(s) ao carrinho.")

    def limpar(self):
        self.itens = []
        self.total = 0.0
