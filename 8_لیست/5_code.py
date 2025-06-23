n = int(input())
colors = list(map(int, input().split()))
counts = {}
for c in colors:
    counts[c] = counts.get(c, 0) + 1
min_count = min(counts.values())
min_colors = [color for color in counts if counts[color] == min_count]
print(min(min_colors))
