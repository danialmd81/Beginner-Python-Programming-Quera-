def print_square(n, c):
    for _ in range(n):
        print(c * n)


def print_squares(n, k, c):
    while n > 0:
        print_square(n, c)
        n -= k


n, k, c = input().split()
n = int(n)
k = int(k)
print_squares(n, k, c)
