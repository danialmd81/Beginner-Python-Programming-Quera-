def hanoi(n, source, target, auxiliary, moves):
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi(n - 1, auxiliary, target, source, moves)


n = int(input())
moves = []
hanoi(n, "A", "C", "B", moves)
for i, (frm, to) in enumerate(moves, 1):
    print(f"{i} {frm} {to}")
