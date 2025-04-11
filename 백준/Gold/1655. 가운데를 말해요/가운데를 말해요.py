import heapq
import sys

input = sys.stdin.readline


class MedianHeap:
    def __init__(self):
        self.over_median = []
        self.under_median = []
        self.size = 0

    # 힙 밸런스를 위해서 두 힙의 크기가 일치하는지 확인
    # 홀수일 경우 중앙값보다 작은 힙이 하나 더 많게
    def is_balanced(self):
        if self.size % 2 == 0:
            return len(self.over_median) == len(self.under_median)
        else:
            return (len(self.over_median) + 1) == len(self.under_median)

    # 어떤 힙이 더 무거운지 계산 후 튜플 쌍으로 return
    # 홀수의 경우를 or로 추가 계산
    def rebalance_targets(self):
        over = len(self.over_median)
        under = len(self.under_median)

        if over > under or (self.size % 2 == 1 and over == under):
            return (self.over_median, self.under_median)

        return (self.under_median, self.over_median)

    # 무거운 힙에서 pop 후, 가벼운 힙에 push
    # 힙을 옮길 땐 무조건 부호가 바뀌니 처리에 주의
    def rebalance(self):
        if self.is_balanced():
            return

        heavy, light = self.rebalance_targets()

        value = -heapq.heappop(heavy)
        heapq.heappush(light, value)

    # 힙에 값을 push
    # 중앙값을 기준으로 넣을 힙을 판별
    # 단, 힙이 비어있다면 작은 쪽에 push (기준값 설정)
    def push(self, value):
        if self.size == 0:
            heapq.heappush(self.under_median, -value)
        else:
            median = self.get_median()
            if value <= median:
                heapq.heappush(self.under_median, -value)
            else:
                heapq.heappush(self.over_median, value)

        self.size += 1
        self.rebalance()

    # 중앙값을 return
    # under_median은 최대힙이니, 부호를 바꿔서 return
    def get_median(self):
        return -self.under_median[0]


N = int(input())
mh = MedianHeap()
result = []

for _ in range(N):
    x = int(input())

    mh.push(x)
    result.append(str(mh.get_median()))

print("\n".join(result))