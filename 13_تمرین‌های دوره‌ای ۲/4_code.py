n, m = map(int, input().split())
flowers = [0] * n

for _ in range(m):
    row = input().strip()
    for i in range(n):
        if row[i] == "W":
            flowers[i] += 1

result = ""
for count in flowers:
    if count % 2 == 1:
        result += "F"
    else:
        result += "B"

print(result)
