from moedas import converterCotacao 

def menu():
    print()
    print('1 - Converter Dólar em Real')
    print('2 - Converter Euro em Real')
    print('3 - Converter Libra em Real')
    print('4 - Outra contação')
    print('0 - Sair')
    print()

opcao = 1

while opcao!= 0:
    menu()
    opcao = int(input('Digite a opção: '))
    
    match opcao:
        case 1: origem = "USD"
        case 2: origem = "GBP"
        case 3: origem = "EUA"
        case 4: 
            ...
            
    print()
    print('******************************************************')
    print(f'O valor de {origem} para BRL:', converterCotacao(origem))
    print('******************************************************')
    print()
    