nums = list(map(int, input().split()))
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
max_count = max(counts.values())
max_notes = [k for k, v in counts.items() if v == max_count]
min_note = min(max_notes)
print(min_note, max_count)
