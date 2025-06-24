a = int(input())
b = int(input())

primes = []
for num in range(a + 1, b):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(str(num))

print(",".join(primes))
