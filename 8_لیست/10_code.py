n, m = map(int, input().split())
count = 0
for _ in range(n):
    row = input().strip()
    count += row.count("*")
print(count)
