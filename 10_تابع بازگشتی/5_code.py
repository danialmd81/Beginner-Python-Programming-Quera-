def count_sequences(n, last1=0, last2=0):
    if n == 0:
        return 1
    res = 0
    # Add 1
    res += count_sequences(n - 1, 0, last1)
    # Add 0 if not three consecutive zeros
    if last1 < 2:
        res += count_sequences(n - 1, last1 + 1, last2)
    return res


n = int(input())
print(count_sequences(n))
