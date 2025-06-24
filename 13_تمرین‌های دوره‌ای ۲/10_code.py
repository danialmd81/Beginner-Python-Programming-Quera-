n = int(input())
a = list(map(int, input().split()))


def check():
    for i in range(n):
        # قله: چپ غیرکاهشی، راست کاملاً کاهشی
        left = all(a[j] <= a[j + 1] for j in range(i))
        right = all(a[j] > a[j + 1] for j in range(i, n - 1))
        if left and right:
            return True
        # دره: چپ غیر افزایشی، راست کاملاً افزایشی
        left = all(a[j] >= a[j + 1] for j in range(i))
        right = all(a[j] < a[j + 1] for j in range(i, n - 1))
        if left and right:
            return True
    return False


print("Yes" if check() else "No")
