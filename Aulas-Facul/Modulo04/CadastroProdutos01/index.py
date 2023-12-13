from classes.Produto import Produto

def menu():
    print()
    print("1 - Listar Produtos")
    print("2 - Inserir Produtos")
    print("3 - Alterar Produtos")
    print("4 - Excluir Produtos")
    print("0 - Sair")
    print()
    
opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção:'))
    
    match opcao:
        case 1:
            Produto.Listartodos()
        case 2:
            codigo = input("Digite o código: ")
            nome = input("Nome do produto: ")
            quantidade = input("Quantidade: ")
            valor = input("Valor do produto: ")
            
            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3:
            Produto.Listartodos()
            selecionado = int(input("Qual item deseja alterar?"))
            item = Produto.Consultar(selecionado)
            
            quantidade = int(input("Qual a nova quantidade: "))
            valor = int(input("Qual o novo valor: "))
            
            produto = Produto(item["codigo"], item["nome"], quantidade, valor)
            produto.Alterar(selecionado)
        case 4:
            Produto.Listartodos()
            selecionado = int(input("Qual item deseja excluir?"))
            Produto.Excluir(selecionado)
        case 0:
            break
