from p import Produto,CarrinhoCompras

carrinho = CarrinhoCompras()

nome = input ('Digite o Produto 1: ')
valor = float(input ('Digite o Valor do Produto 1: ')) 
produto_1 = Produto(nome,valor)

nome = input ('Digite o Produto 2: ')
valor = float(input ('Digite o Valor do Produto 2: '))
produto_2 = Produto(nome,valor)

nome = input ('Digite o Produto 3: ')
valor = float(input ('Digite o Valor do Produto 3: '))
produto_3 = Produto(nome,valor)

carrinho.inserir_produto(produto_1)
carrinho.inserir_produto(produto_2)
carrinho.inserir_produto(produto_3)


print(carrinho.soma_total())
