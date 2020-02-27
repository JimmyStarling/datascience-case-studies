# Crescimento da População Brasileira 1980-2016
# DataSUS

import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")  
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x, y, color="#000000", linewidth=2, linestyle="--")
plt.bar(x, y, color="#CCCCCC")
plt.title("Crescimento da população Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()  
#plt.savefig("Populacao_brasileira.png", dpi=300)
