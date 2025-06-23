with open("my_belladi_code.txt", "r") as f:
    n = int(f.readline())
    total = 0
    for _ in range(n):
        total += int(f.readline())
print(total)
