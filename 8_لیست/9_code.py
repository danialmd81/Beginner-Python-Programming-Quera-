n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    row = [A[i][j] + B[i][j] for j in range(m)]
    print(" ".join(map(str, row)))
