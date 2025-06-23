def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1


a = int(input())
b = int(input())
for num in range(a, b + 1):
    if is_prime(num):
        print(num)
