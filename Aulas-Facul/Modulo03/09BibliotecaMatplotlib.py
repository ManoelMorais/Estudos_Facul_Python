import matplotlib.pyplot as plt

# meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]

# qtdTI = [70, 98, 30, 37, 55, 112, 86, 12, 23, 33, 68, 44]
# qtdRH = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


# plt.plot(meses, qtdTI, label="TI", color="blue", linestyle="-", marker="o")
# plt.plot(meses, qtdRH, label="RH", color="red",  linestyle="--", marker=".")
# plt.bar(meses, qtdTI, label="TI", color="blue")
# plt.bar(meses, qtdRH, label="RH", color="red")
# plt.title("Chamadas abertos")
# plt.xlabel("Meses")
# plt.ylabel("Valores")
# plt.legend()
# # plt.show()

navegadores = ['chrome', 'FireFox', 'Edge', 'Safare']
qtd = [4000, 1000, 2000, 3000]
cores = ['red', 'orange', 'blue', 'light blue']

plt.pie(qtd, labels=navegadores, colors=cores)
plt.show()

