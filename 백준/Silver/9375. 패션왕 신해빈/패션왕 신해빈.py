from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dress = defaultdict(int)

    N = int(input())
    for i in range(N):
        name, part = input().split()
        dress[part] += 1

    answer = 1
    for part, count in dress.items():
        answer *= count + 1

    print(answer - 1)
