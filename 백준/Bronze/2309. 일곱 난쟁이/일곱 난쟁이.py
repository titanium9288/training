def solution(dwarfs):
    for d1 in dwarfs:
        for d2 in dwarfs:
            if d1 == d2:
                continue
            if sum(dwarfs) - (d1 + d2) == 100:
                return [str(item) for item in sorted(dwarfs) if item not in [d1, d2]]


dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

print("\n".join(solution(dwarfs)))