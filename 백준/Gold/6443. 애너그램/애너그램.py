from collections import Counter


def backtrack(path):
    if len(path) == len(letter):
        key = "".join(path)
        if key not in visited:
            visited.add(key)
            anagrams.append(key)
        return

    for c in sorted(counter):
        if counter[c] > 0:
            path.append(c)
            counter[c] -= 1

            backtrack(path)

            path.pop()
            counter[c] += 1


N = int(input())
for _ in range(N):
    letter = input()
    counter = Counter(letter)
    visited = set()
    anagrams = []

    backtrack([])
    print("\n".join(anagrams))
