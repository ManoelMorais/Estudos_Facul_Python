
try: 
    n1 = int(input("Valor: "))
    n2 = int(input("Divisor: "))
    
    res = n1 / n2
    
    print(f"O resultado da divisão é {res}")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}") 
    
except ValueError:
    print(f"Ocorreu um erro") 

except ZeroDivisionError:
    print(f"Somente número que não divida por 0") 
    
else:
    print("Ocorreu algum erro na divisão") 
    
finally:
    print("Fim")