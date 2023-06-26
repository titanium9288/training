# 테스트 케이스의 갯수
N = int(input())

# [걸리는 시간, 수익]
cases = [0]
for _ in range(N):
    cases.append(list(map(int, input().split())))

incomes_list = [0 for _ in range(N + 2)]

for i in range(1, N + 1):
    # 기본적으로 전날의 수익과 같음
    incomes_list[i] = max(incomes_list[i], incomes_list[i - 1])
    period = cases[i][0]
    pay = cases[i][1]

    # 해당 일을 할 수 있는 경우에만
    if i + period <= N + 1:
        incomes_list[i + period] = max(incomes_list[i + period], incomes_list[i] + pay)

print(max(incomes_list))
