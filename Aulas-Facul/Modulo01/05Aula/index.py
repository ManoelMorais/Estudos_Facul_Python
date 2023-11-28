day = int(input("Digita o número do dia da semana"))
#int e para deixar o numero e não string

if day == 1:
    print("Domingo")
elif day == 2:
    print("Segunda")
elif day == 3:
    print("Terça")
elif day == 4:
    print("Quarta")
elif day == 5:
    print("Quinta")
elif day == 6:
    print("Sexta")
elif day == 7:
    print("Sabado")
else:
    print("this day is not exist")

match day:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case other:
        print("this day is not exist")