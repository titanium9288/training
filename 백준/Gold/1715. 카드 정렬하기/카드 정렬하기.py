import heapq
import sys

input = sys.stdin.readline

N = int(input())
answer = 0

cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)


while len(cards) != 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    card3 = card1 + card2
    answer += card3

    heapq.heappush(cards, card3)

print(answer)
