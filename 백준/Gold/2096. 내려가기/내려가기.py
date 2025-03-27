import sys

input = sys.stdin.readline

N = int(input())

prev_max = [0, 0, 0]
prev_min = [0, 0, 0]

new_max = [0, 0, 0]
new_min = [0, 0, 0]

for _ in range(N):
    current = list(map(int, input().split()))

    for i in range(3):
        new_max[i] = (
            max(prev_max[j] for j in range(max(0, i - 1), min(3, i + 2))) + current[i]
        )
        new_min[i] = (
            min(prev_min[j] for j in range(max(0, i - 1), min(3, i + 2))) + current[i]
        )

    prev_max = new_max[:]
    prev_min = new_min[:]

print(max(prev_max), min(prev_min))
