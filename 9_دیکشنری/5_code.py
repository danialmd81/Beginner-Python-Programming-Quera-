students = []
scores = []

while True:
    s = input()
    if s == "End":
        break
    name, score = s.split()
    score = float(score)
    students.append((name, score))
    scores.append(score)

if scores:
    avg = sum(scores) / len(scores)
    accepted = [name for name, score in students if score >= avg]
    print(accepted)
    if accepted:
        accepted_scores = [score for name, score in students if score >= avg]
        print(sum(accepted_scores) / len(accepted_scores))
    else:
        print(0)
else:
    print([])
    print(0)
