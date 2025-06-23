# شمارش امتیازها
score_bijan = 0
score_behrooz = 0
score_mohsen = 0

while True:
    a, b, c = map(int, input().split())
    if a == b == c:
        break
    min_val = min(a, b, c)
    # اگر فقط یک نفر کمترین مقدار را دارد، امتیاز می‌گیرد
    if a == min_val and a != b and a != c:
        score_bijan += 1
    elif b == min_val and b != a and b != c:
        score_behrooz += 1
    elif c == min_val and c != a and c != b:
        score_mohsen += 1

if score_bijan > score_behrooz and score_bijan > score_mohsen:
    print("Eyval Bijan!")
else:
    print("Ey baba! Eshkal nadare.")
