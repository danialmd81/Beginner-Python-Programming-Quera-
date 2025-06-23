# جدول ضرب جادویی 1 تا 10
for i in range(1, 11):
    row = []
    for j in range(1, 11):
        if i > j:
            row.append(str(i * j))
        elif i == j:
            row.append("0")
        else:
            row.append(str(-(i * j)))
    print(" ".join(row))
