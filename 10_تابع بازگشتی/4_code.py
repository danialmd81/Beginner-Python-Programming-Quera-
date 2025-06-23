n = int(input())


def josephus(n):
    if n == 1:
        return 1
    return (josephus(n - 1) + 1) % n + 1


print(josephus(n))
