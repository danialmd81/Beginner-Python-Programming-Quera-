s = input().strip()
p = input().strip()
indices = []
for i in range(len(s) - len(p) + 1):
    if s[i : i + len(p)] == p:
        indices.append(i + 1)
print(*indices)
