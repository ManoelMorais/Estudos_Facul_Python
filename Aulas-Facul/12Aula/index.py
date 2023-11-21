arquivo = open('pessoas.txt', 'a+') # "w" substitui a cada mudança, muda o arquivo todo, "a+" so add sem modificar todo o arquivo

arquivo.write('João\n')
arquivo.write('Manoel\n')
arquivo.write('Maria\n')
arquivo.write('Clara\n')

arquivo.close()


with open('pessoas.txt', 'r+' ) as arquivoleitura:
    
    for linha in arquivoleitura:
        print(linha)
