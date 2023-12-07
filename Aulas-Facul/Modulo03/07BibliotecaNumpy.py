import numpy as np

numeros = [1,2,3,4,5,6,7,8]

soma = 0

for n in numeros:
    soma += n
    
media =  soma / len(numeros)
print("media na mão", media)


array_numeros = np.array(numeros)
Media = np.mean(array_numeros)
print("Meidia com o numpy", Media)


