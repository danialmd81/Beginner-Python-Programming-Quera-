n = int(input())
arr = list(map(int, input().split()))
flag = 0

for i in range(n):
    if arr[i] == 4:
        flag += 1
        if flag == 2:
            print(i + 1)
            break
else:
    print(-1)
