def sum_digits(x):
    return sum(int(d) for d in str(x))


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def sum_prime_factors(x):
    factors = set()
    for i in range(2, x + 1):
        if x % i == 0 and is_prime(i):
            factors.add(i)
    return sum(factors)


def D(x):
    return x + sum_digits(x) + sum_prime_factors(x)


t = int(input())
for _ in range(t):
    n = int(input())
    found = False
    for x in range(1, n):
        if D(x) == n:
            found = True
            break
    print("Yes" if found else "No")
