## 🛒 Anadius Supermercado – Terminal Edition

Sistema de supermercado desenvolvido em Python com interface via terminal e foco total em Programação Orientada a Objetos (POO). Ideal para praticar lógica, classes e interações em tempo real com o usuário. Criado com 💜 e boas práticas!

## Funcionalidades 🧠

- 📦 Cadastro de produtos (nome, preço, estoque)
- 👤 Cadastro de clientes (nome e CPF)
- 🔍 Busca de produtos disponíveis
- 🛒 Carrinho de compras com lista de itens e quantidade
- ❌ Validação de estoque antes da compra
- ✅ Finalização de compra com desconto no estoque
- 🧼 Carrinho é limpo automaticamente após a compra
- 🎯 Reuso com classes bem definidas (Produto, Cliente, Carrinho, Supermercado)

## Tecnologias Utilizadas 💻

- **Linguagem:** Python 3.10+
- **Paradigma:** POO
- **Execução:** Terminal (CLI)
- **Organização:** Separação em arquivos e uso de import

## Estrutura do Projeto 📁
```
AnadiusSupermercado/
├── main.py                # Menu principal e fluxo da aplicação
├── supermercado.py        # Lógica geral do supermercado
├── produto.py             # Classe Produto
├── cliente.py             # Classe Cliente
├── carrinho.py            # Classe Carrinho
└── README.md              # Documentação do projeto
```

## Instruções de Configuração 📋
1. **Clone o repositório:**
```bash
git clone https://github.com/seuusuario/AnadiusSupermercado.git
cd AnadiusSupermercado
```

2. **Execute o programa:**
```bash
python3 main.py
```

## Siga as instruções do menu via terminal 👇
```bash
=== MENU ===
1 - Ver produtos
2 - Adicionar produto ao carrinho
3 - Finalizar compra
4 - Sair

1. Exemplo de Fluxo 🧾

Digite o nome do cliente: Beatriz
Digite o CPF do cliente: 876.904.300-87

Produtos disponíveis:
Arroz - R$ 5.90 (Estoque: 10)
Feijão - R$ 6.20 (Estoque: 8)

Nome do produto: Arroz
Quantidade: 2

Venda realizada com sucesso para o cliente 'Beatriz'!
```

## Boas Práticas Adotadas ✅
- Organização por responsabilidade de classe
- Separação clara entre lógica de negócio e interface
- Uso correto de encapsulamento e construtores
- Padronização dos nomes de métodos e atributos
- Padrão de commits semânticos (feat:, fix:, docs: etc)

## Próximas Melhorias 📌
- [] Adicionar opção para remover item do carrinho
- [] Histórico de compras por cliente
- [] Exportar relatório de vendas em .txt ou .csv
- [] Cadastro de novos produtos em tempo real

## Contribuindo 🤝
Se você quiser contribuir com o projeto, siga os seguintes passos:

1. Faça um Fork deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b minha-feature`).
3. Commit suas mudanças (`git commit -am 'Adicionando nova feature'`).
4. Push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença 📜
Este projeto está sob a licença MIT. Sinta-se livre para usar e adaptar!


## Desenvolvido por Vitória Mota 👩🏼‍💻
