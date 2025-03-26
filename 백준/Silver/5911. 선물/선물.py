N, B = map(int, input().split())
presents = []
answer = 0

for i in range(N):
    P, S = map(int, input().split())
    presents.append((P, S))

original_cost = [p + s for p, s in presents]

for i in range(N):
    after_sale_cost = original_cost[:]

    # 각 선물에 대해 할인 적용
    P, S = presents[i]
    after_sale_cost[i] = P // 2 + S

    after_sale_cost.sort()
    count = 0
    budget = B

    for cost in after_sale_cost:
        budget -= cost
        if budget < 0:
            break

        count += 1

    # 최대값 갱신
    if answer < count:
        answer = count

print(answer)
