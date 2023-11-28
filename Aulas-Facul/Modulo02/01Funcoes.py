def dividir(num1, num2):
    if num2 == 0:
        print("Não é possivel dividir um número por 0")
    else:
        resu = num1 / num2
        # print(f'O resultado de {num1} / {num2} = {resu}')
        return resu
    
divisao = dividir(80, 5)
print("O resultado da divisão é", divisao)

print("divisão", dividir(450, 5))

resultado = dividir(3, 1)
soma = 20 + resultado
print("A soma é", soma)

dividir(6, 0)
