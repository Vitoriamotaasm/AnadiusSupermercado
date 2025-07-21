from supermercado import Supermercado
from carrinho import Carrinho
from cliente import Cliente

def menu():
    print("\n=== MENU ===")
    print("1 - Ver produtos")
    print("2 - Adicionar produto ao carrinho")
    print("3 - Finalizar compra")
    print("4 - Sair")

def main():
    mercado = Supermercado()
    carrinho = Carrinho()
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    mercado.cadastrarCliente(nome, cpf)
    cliente = mercado.clientes[nome]


    # Exemplo de produtos cadastrados previamente
    mercado.cadastrarProduto("Arroz", 5.90, 10)
    mercado.cadastrarProduto("Feijão", 6.20, 8)
    mercado.cadastrarProduto("Macarrão", 4.80, 5)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nProdutos disponíveis:")
            for produto in mercado.produtos.values():
                print(f"{produto.nome} - R$ {produto.preco:.2f} (Estoque: {produto.estoque})")

        elif opcao == "2":
            nome = input("Nome do produto: ")
            if nome not in mercado.produtos:
                print(f"Produto '{nome}' não encontrado.")
                continue
            quantidade = int(input("Quantidade: "))
            produto = mercado.produtos[nome]
            carrinho.adicionar(produto, quantidade)

        elif opcao == "3":
            mercado.realizarVenda(cliente, carrinho)
            carrinho.limpar()

        elif opcao == "4":
            print("Encerrando sistema... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
