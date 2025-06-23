n = int(input())
max_unique = 0
for _ in range(n):
    name = input().strip()
    unique_letters = len(set(name))
    if unique_letters > max_unique:
        max_unique = unique_letters
print(max_unique)
