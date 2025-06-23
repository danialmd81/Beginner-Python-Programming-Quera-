input_str = input()
a1, a2, a3 = map(int, input_str.split())
if (a1 + a2 + a3 == 180 and a1 > 0 and a2 > 0 and a3 > 0) and (
    a1 == 90 or a2 == 90 or a3 == 90
):
    print("Bale")
else:
    print("Na")
