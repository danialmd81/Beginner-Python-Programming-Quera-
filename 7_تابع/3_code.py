def print_square(n):
    for _ in range(n):
        print("*" * n)


def print_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)


n, ch = input().split()
n = int(n)
if ch == "s":
    print_square(n)
elif ch == "t":
    print_triangle(n)
