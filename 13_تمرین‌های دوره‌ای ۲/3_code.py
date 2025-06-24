n = int(input())
s1 = input()
s2 = input()

count = 0
for i in range(n):
    if s1[i] != s2[i]:
        count += 1

print(count)
