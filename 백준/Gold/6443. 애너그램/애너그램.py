from collections import Counter


def backtrack(path):
    if len(path) == len(letter):
        anagrams.append("".join(path))
        return

    for c in sorted(letter):
        if counter[c] > 0:
            path.append(c)
            counter[c] -= 1

            key = tuple(path)
            if not key in visited:
                visited.add(key)
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