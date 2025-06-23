n, q = map(int, input().split())
nums = set(map(int, input().split()))
for _ in range(q):
    _, x = input().split()
    x = int(x)
    print(1 if x in nums else 0)
