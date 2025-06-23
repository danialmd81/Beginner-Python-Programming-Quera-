def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_list(nums):
    result = nums[0]
    for n in nums[1:]:
        result = gcd(result, n)
    return result


nums = list(map(int, input().split()))
print(gcd_list(nums))
