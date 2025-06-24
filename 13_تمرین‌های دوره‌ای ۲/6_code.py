n, k = map(int, input().split())
feet = []
for i in range(1, n + 1):
    feet.append(i)
    feet.append(i)

start = 0
while True:
    # اگر فقط دو پای یک نفر باقی مانده یا فقط یک پا باقی مانده، بازی تمام است
    if (len(feet) == 2 and feet[0] == feet[1]) or len(feet) == 1:
        print(f"winner:{feet[0]}")
        break
    for i in range(k):
        print(feet[(start + i) % len(feet)], end=" ")
    print()
    remove_index = (start + k - 1) % len(feet)
    del feet[remove_index]
    if len(feet) == 0:
        break
    if remove_index == len(feet):
        start = 0
    else:
        start = remove_index
