def somar(n1, n2):
    return n1 + n2

def subtr(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divid(n1, n2):
    if n2 == 0:
        "Não é possivel dividir por 0"
    else:
        return n1 / n2


def calcular(n1, n2, operador):
    match operador:
        case '+': return somar(n1, n2)
        case '-': return subtr(n1, n2)
        case '*': return multi(n1, n2)
        case '/': return divid(n1, n2)    
        case other: return 'Operador não encontrado'


print(calcular(5, 10, '+'))
print(calcular(5, 10, '-'))
print(calcular(5, 10, '*'))
print(calcular(5, 0, '/'))
print(calcular(5, 10, 'o'))