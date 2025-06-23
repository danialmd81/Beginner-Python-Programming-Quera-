n, q = map(int, input().split())
nums = list(map(int, input().split()))


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


for _ in range(q):
    _, x = input().split()
    x = int(x)
    print(1 if binary_search(nums, x) else 0)
