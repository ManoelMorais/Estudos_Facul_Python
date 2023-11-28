numeros = [1, 3, 8, 5, 10]

# Teste 01
resu = []
for n in numeros:
     resu.append(n*2)
    
print(resu)


# Teste 02
def mult(n1):
    return n1 * 2

resultado = map(mult, numeros)
print(numeros, list(resultado))


# Teste 03
result = map(lambda n: n * 2, numeros)
print(numeros, list(result))

