t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x == y and x % 2 == 0:
        print(2 * x)
    elif x == y and x % 2 == 1:
        print(2 * x - 1)
    elif x == y + 2 and x % 2 == 0:
        print(2 * x - 2)
    elif x == y + 2 and x % 2 == 1:
        print(2 * x - 3)
    else:
        print(-1)
