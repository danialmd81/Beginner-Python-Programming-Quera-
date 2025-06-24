with open("my_belladi_code.txt", "r") as file:
    n = int(file.readline().strip())
    total = 0
    for _ in range(n):
        number = int(file.readline().strip())
        total += number
    print(total)
