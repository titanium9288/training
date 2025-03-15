import sys

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]

for i in range(len(numbers)):
    prefix_sum.append(prefix_sum[i] + numbers[i])

input_query = sys.stdin.read().split()
answer = []

for a in range(M):
    i = int(input_query[a * 2])
    j = int(input_query[a * 2 + 1])
    answer.append(str(prefix_sum[j] - prefix_sum[i - 1]))

sys.stdout.write("\n".join(answer))
