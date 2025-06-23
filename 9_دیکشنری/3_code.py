s = input()
chars = [".", "?", "!", ",", "/", "-", "+"]
count = {c: 0 for c in chars}

for ch in s:
    if ch in count:
        count[ch] += 1

print(count)
