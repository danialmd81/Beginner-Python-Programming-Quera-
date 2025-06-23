# دریافت عدد n
n = int(input())
total = 0
for i in range(1, n + 1):
    step_sum = 0
    expr = ""
    for j in range(1, i + 1):
        step_sum += j
        expr += str(j)
        if j != i:
            expr += "+"
    print(f"{expr} = {step_sum}")
    total += step_sum
print(f"Total sum of series is: {total}")
