n_linhas = 3
n_colunas = 5
m = [[0 for c in range(n_colunas)]
        for l in range(n_linhas)]
for l in range(n_linhas):
    for c in range(n_colunas):
        m[l][c] = int(input())
print(m)