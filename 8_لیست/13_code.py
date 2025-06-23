n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    t, left, r = map(int, input().split())
    left -= 1  # تبدیل به اندیس صفرم‌بنیان
    r -= 1
    if t == 1:
        print(sum(arr[left : r + 1]))
    else:
        arr[left : r + 1] = [arr[r]] + arr[left:r]
