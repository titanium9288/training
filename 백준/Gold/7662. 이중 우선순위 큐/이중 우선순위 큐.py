from collections import Counter
import heapq
import sys


input = sys.stdin.readline


class DualQueue:
    def __init__(this, k):
        this.min_queue = []
        this.max_queue = []

        this.length = 0
        this.valid_value = [True] * k

    def push(this, n, id):
        heapq.heappush(this.min_queue, (n, id))
        heapq.heappush(this.max_queue, (-n, id))

        this.length += 1

    def pop(this, n):
        if this.length == 0:
            return None

        target_queue = this.min_queue if n == -1 else this.max_queue

        while target_queue:
            delete_value, id = heapq.heappop(target_queue)
            delete_value = -delete_value * n

            if not this.valid_value[id]:
                continue

            this.valid_value[id] = False
            return delete_value

    def clean_queue(this):
        if this.length != 0:
            return None

        this.min_queue = []
        this.max_queue = []

    def result(this):
        if this.length == 0:
            return "EMPTY"
        min_value, max_value = None, None

        while this.min_queue:
            i, id = heapq.heappop(this.min_queue)
            if this.valid_value[id]:
                min_value = i
                break

        while this.max_queue:
            i, id = heapq.heappop(this.max_queue)
            if this.valid_value[id]:
                max_value = -i
                break

        if min_value is not None and max_value is not None:
            return f"{max_value} {min_value}"
        else:
            return "EMPTY"


T = int(input())

for _ in range(T):
    k = int(input())
    dq = DualQueue(k)
    id = 0

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == "I":
            dq.push(num, id)
            id += 1

        if op == "D":
            dq.pop(num)

    print(dq.result())
