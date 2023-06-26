import sys


def fixed_round(number):
    if number % 1 == 0.5:
        return round(number + 0.1, 0)
    else:
        return round(number, 0)


# 의견의 갯수
N = int(input())

difficulties = []
for _ in range(N):
    difficulties.append(int(sys.stdin.readline().rstrip()))

difficulties.sort()

# 절사평균을 위해 15%를 자르기
extreme_value = int(fixed_round(N * 0.15))
cut_N = N - (2 * extreme_value)

final_difficulty = int(
    fixed_round(sum(difficulties[extreme_value : (N - extreme_value)]) / cut_N)
    if N != 0
    else 0
)

print(final_difficulty)
