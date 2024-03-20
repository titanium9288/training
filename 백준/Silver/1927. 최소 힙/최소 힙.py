import sys


class heap:
    def __init__(self):
        self.heap = []

    def enqueue(self, n):
        self.heap.append(n)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i - 1) // 2] > self.heap[i]:
            self.heap[(i - 1) // 2], self.heap[i] = (
                self.heap[i],
                self.heap[(i - 1) // 2],
            )
            i = (i - 1) // 2

    def heapify(self, i):
        min = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[min]:
            min = left
        if right < len(self.heap) and self.heap[right] < self.heap[min]:
            min = right

        if min != i:
            self.heap[i], self.heap[min] = self.heap[min], self.heap[i]
            self.heapify(min)

    def dequeue(self):
        if len(self.heap) == 0:
            return 0
        min = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return min

    def get_heap(self):
        return self.heap


N = int(sys.stdin.readline())
h = heap()
for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        print(h.dequeue())
    else:
        h.enqueue(x)