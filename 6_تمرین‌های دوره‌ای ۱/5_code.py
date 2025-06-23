r, c = map(int, input().split())
row_from_top = 11 - r
if 1 <= c <= 10:
    direction = "Right"
    seat_from_entry = 11 - c
else:
    direction = "Left"
    seat_from_entry = c - 10 + 1
print(f"{direction} {row_from_top} {seat_from_entry}")
