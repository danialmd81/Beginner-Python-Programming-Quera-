def f1(n):
    global score
    score += n
    return 0


def f2(n):
    global score
    score -= n
    return 0


def f3(n):
    score = n
    return score


score = int(input())
print(f2(10))
print(score)
print(f1(5))
print(score)
print(f3(12))
print(score)
print(f1(2))
print(score)
