# i = 1
continuar = True

while continuar: 

    numero = int(input("Qual número da tabuada?"))

    for i in range(1, 11): 
        print(f"{numero} x {i} = {2*i}")
    
    continuar = input("Deseja continuar? (s/n)")
    continuar = True if continuar == "s" else False





# print(f"2 x {i} = {2*i}")
#     # forma 1
#     # i = i + 1
#     #  forma 2
#     i += 1