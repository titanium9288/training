import sys

input = sys.stdin.readline
PRIME_MOD = 1000000007


class SegmentTree:
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

            self.left = SegmentTree(arr, start, mid)
            self.right = SegmentTree(arr, mid + 1, end)
            self.value = (self.left.value * self.right.value) % PRIME_MOD

    def update(self, idx, value):
        start = self.start
        end = self.end

        if start == end:
            self.value = value
            return

        mid = (self.start + self.end) // 2
        if idx > mid:
            self.right.update(idx, value)
        else:
            self.left.update(idx, value)

        self.value = (self.left.value * self.right.value) % PRIME_MOD

    def query(self, start, end):
        if self.start >= start and self.end <= end:
            return self.value
        elif self.start > end or self.end < start:
            return 1
        else:
            left_query = self.left.query(start, end)
            right_query = self.right.query(start, end)
            return (left_query * right_query) % PRIME_MOD


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = SegmentTree(arr)
answer = []

for _ in range(M + K):
    a, b, c = map(int, input().split())

    # a가 1일 경우 b번째 수를 c로 바꾼다
    if a == 1:
        tree.update(b - 1, c)

    # a가 2일 경우, b부터 c까지의 곱을 구한다
    if a == 2:
        answer.append(str(tree.query(b - 1, c - 1)))

print("\n".join(answer))
