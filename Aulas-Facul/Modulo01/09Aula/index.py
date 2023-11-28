numeros = [1,2,3,4,5,6,7,8,9]
pessoas = ["João", "Maria", "Luiza", "Carlos"]

print(numeros[4]) #escolher a posição []
print(pessoas[1])

print(len(numeros))
print(len(pessoas)) # quantidade de oobjetos no array

pessoas.append("luiz") # add
print(pessoas)

pessoas.remove("Maria") # remover da lista sabendo o nome
print(pessoas)

del pessoas[2] # remover da lista sem saber o nome
print(pessoas)

pessoas = sorted(pessoas)# ordenar
print(pessoas)

for i in pessoas:
    print(i)
