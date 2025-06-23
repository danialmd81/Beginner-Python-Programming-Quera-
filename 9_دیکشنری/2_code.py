players = input().split()
scores = {name: 0 for name in players}

while True:
    s = input()
    if s == "End":
        break
    name, point = s.split()
    scores[name] += int(point)

max_score = max(scores.values())
for name in players:
    if scores[name] == max_score:
        print(name)
