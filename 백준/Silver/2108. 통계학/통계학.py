import sys

# 총 숫자의 갯수 N
N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort()

# 산술평균
mean = int(round(sum(numbers) / N, 0))
print(mean)

# 중앙값
median = numbers[N // 2]
print(median)

# 최빈값
count_dict = {}

# 중복이 없는 숫자의 갯수를 구한 후
for number in numbers:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

# 가장 많이 나온 숫자들을 추려서
max_count = max(count_dict.values())
mode_list = [key for key, value in count_dict.items() if value == max_count]

# 여러개 있을 땐 두 번째로 작은 값을 출력.
print(mode_list[int(len(mode_list) > 1)])

# 범위
number_range = numbers[-1] - numbers[0]
print(number_range)
