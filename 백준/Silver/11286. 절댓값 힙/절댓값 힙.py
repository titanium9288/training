import heapq
import sys

input = sys.stdin.readline


def abs_heap(x):
    # x가 0일때 heappop
    if x == 0:
        if not queue:
            return 0

        _, val = heapq.heappop(queue)
        return val

    else:
        heapq.heappush(queue, (abs(x), x))


N = int(input())
queue = []

answer = []
for _ in range(N):
    x = int(input())

    val = abs_heap(x)
    if val is not None:
        answer.append(str(val))

print("\n".join(answer))
