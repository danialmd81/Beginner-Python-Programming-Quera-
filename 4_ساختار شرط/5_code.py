input_str = input()
a1, a2, a3 = map(int, input_str.split())
max = a1
sum = a2 + a3
if a2 > max:
    max = a2
    sum = a1 + a3
if a3 > max:
    max = a3
    sum = a2 + a1
if sum > max:
    print("Bale")
else:
    print("Na")
