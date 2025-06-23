en = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
fr = {1: "Un", 2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq"}

while True:
    s = input()
    if s == "End":
        break
    num, lang = s.split()
    num = int(num)
    if lang == "En":
        print(en[num])
    else:
        print(fr[num])
