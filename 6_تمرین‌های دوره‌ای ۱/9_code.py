n, k = map(int, input().split())
current = 1
steps = 0
while True:
    steps += 1
    current = (current + k - 1) % n + 1
    if current == 1:
        break
print(steps)
