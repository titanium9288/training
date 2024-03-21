candidates = []
for _ in range(int(input())):
    candidates.append(int(input()))

buy = 0
if len(candidates) > 1:
    while candidates[0] <= max(candidates[1:]):
        candidates[candidates[1:].index(max(candidates[1:])) + 1] -= 1
        candidates[0] += 1
        buy += 1

print(buy)