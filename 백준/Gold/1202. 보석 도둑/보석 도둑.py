import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = [tuple(map(int, input().split())) for _ in range(N)]
jewel = sorted(jewel, reverse=True)

bags = [int(input()) for _ in range(K)]
heap = []
total_price = 0

for bag in sorted(bags):
    # 현재 가방에 담을 수 있는 보석들을 힙에 넣기
    while jewel:
        weight, price = jewel.pop()

        # 조건에 맞지 않는 보석은 돌려놓기
        if weight > bag:
            jewel.append((weight, price))
            break

        heapq.heappush(heap, -price)

    # 담을 수 있는 보석 중 가장 비싼 걸 선택
    if heap:
        total_price += -heapq.heappop(heap)

print(total_price)
