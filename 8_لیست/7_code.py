q = int(input())
arr = []
for _ in range(q):
    cmd = input().split()
    if cmd[0] == "+":
        i = int(cmd[1]) - 1
        x = int(cmd[2])
        arr.insert(i, x)
    else:  # cmd[0] == '-'
        i = int(cmd[1]) - 1
        arr.pop(i)
    if arr:
        print(" ".join(map(str, arr)))
    else:
        print("EMPTY")
