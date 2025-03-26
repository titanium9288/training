import sys
input = sys.stdin.readline

N = int(input())
houses = []

for i in range(N):
    house = list(map(int, input().split()))
    houses.append(house)

houses.sort(key=lambda x: (x[0], x[1]))

min_cost = houses[0][1]
result = 1

for i in range(1, N):
    house = houses[i]

    # 거리-가격순 정렬이므로, 이전 집과 거리가 동일하다면 자동으로 배제
    if house[0] == houses[i - 1][0]:
        continue

    # 현재 min_cost보다 싸다면, result를 +1 하고 최소 가격을 갱신
    if house[1] < min_cost:
        min_cost = house[1]
        result += 1

print(result)
