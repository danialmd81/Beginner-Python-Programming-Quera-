n, m = map(int, input().split())
magic = [[0] * n for _ in range(n)]

i, j = 0, n // 2
for k in range(m, m + n * n):
    magic[i][j] = k
    ni, nj = (i - 1) % n, (j + 1) % n
    if magic[ni][nj]:
        i = (i + 1) % n
    else:
        i, j = ni, nj

for row in magic:
    print(" ".join(map(str, row)))
