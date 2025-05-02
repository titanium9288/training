N = int(input())
road = list(map(int, input().split())) + [0]
price = list(map(int, input().split()))

selected = float("inf")
total = 0

for i in range(N):
    if price[i] < selected:
        selected = price[i]

    total += selected * road[i]

print(total)