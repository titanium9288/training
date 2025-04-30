import sys

input = sys.stdin.readline


class MinSegmentTree:
    def __init__(self, arr, start=0, end=None):
        self.arr = arr
        if end is None:
            end = len(arr) - 1

        self.start = start
        self.end = end
        self.left = None
        self.right = None

        if start == end:
            self.value = arr[start]
        else:
            mid = (start + end) // 2

            self.left = MinSegmentTree(arr, start, mid)
            self.right = MinSegmentTree(arr, mid + 1, end)
            self.value = min(self.left.value, self.right.value)

    def query(self, start, end):
        if self.start >= start and self.end <= end:
            return self.value
        elif self.start > end or self.end < start:
            return float("inf")
        else:
            left_query = self.left.query(start, end)
            right_query = self.right.query(start, end)
            return min(left_query, right_query)


class MaxSegmentTree:
    def __init__(self, arr, start=0, end=None):
        self.arr = arr
        if end is None:
            end = len(arr) - 1

        self.start = start
        self.end = end
        self.left = None
        self.right = None

        if start == end:
            self.value = arr[start]
        else:
            mid = (start + end) // 2

            self.left = MaxSegmentTree(arr, start, mid)
            self.right = MaxSegmentTree(arr, mid + 1, end)
            self.value = max(self.left.value, self.right.value)

    def query(self, start, end):
        if self.start >= start and self.end <= end:
            return self.value
        elif self.start > end or self.end < start:
            return -float("inf")
        else:
            left_query = self.left.query(start, end)
            right_query = self.right.query(start, end)
            return max(left_query, right_query)


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

min_tree = MinSegmentTree(arr)
max_tree = MaxSegmentTree(arr)
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    answer.append(f"{min_tree.query(a-1, b-1)} {max_tree.query(a-1, b-1)}")

print("\n".join(answer))
