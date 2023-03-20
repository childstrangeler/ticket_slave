salnr = []
rækker = []
sæder = []


salnr.append("sal_1")
salnr.append("sal_2")

for i in salnr:
    if i == "sal_1":
        rækker = 5
        sæder = 10

    if i == "sal_2":
        rækker = 6
        sæder = 12

    sæder_ialt = sæder*rækker
    print(i, "har", rækker, "rækker, og", sæder,
          "sæder. Der er i alt", sæder_ialt, "sæder i salen")

[a*b for (a, b) in zip(rækker, sæder)]
rows = 3
columns = 4
mat = [[0 for row in range(rows)] for col in range(columns)]
mat[col][row] = 1

mat = [[0, 0, 0, 0], [0, 0, 0, 0]]
