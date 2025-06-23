n = int(input())
students = []
for i in range(n):
    name = input().strip()
    grades = list(map(float, input().split()))
    k, scores = int(grades[0]), grades[1:]
    avg = sum(scores) / k
    avg_int = int(avg)
    sports = input().split()
    sports_count = int(sports[0])
    students.append((-avg_int, -sports_count, i, name))
# مرتب‌سازی بر اساس معیارها
students.sort()
for s in students:
    print(s[3])
