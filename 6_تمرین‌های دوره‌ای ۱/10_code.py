n, k = map(int, input().split())
numbers = list(map(int, input().split()))
if any(a > k for a in numbers):
    print("YES")
else:
    print("NO")
