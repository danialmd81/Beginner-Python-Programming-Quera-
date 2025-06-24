n, b = map(int, input().split())
digits = "0123456789ABCDEF"
if n == 0:
    print(0)
else:
    res = ""
    while n > 0:
        res = digits[n % b] + res
        n //= b
    print(res)
