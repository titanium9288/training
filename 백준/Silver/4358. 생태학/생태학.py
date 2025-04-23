from collections import defaultdict
import sys

counter = defaultdict(int)
total_count = 0

while True:
    tree = sys.stdin.readline()
    if not tree:
        break
    tree = tree.rstrip()

    counter[tree] += 1
    total_count += 1

for tree in sorted(counter.keys()):
    ratio = counter[tree] / total_count * 100
    print(f"{tree} {ratio:.4f}")
