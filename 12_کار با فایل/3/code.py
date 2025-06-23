with open("entry_file.txt", "r+") as f:
    n = int(f.readline())
    f.seek(n)
    f.write("#\n")
