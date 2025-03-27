N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

window_sum = sum(temperatures[:K])
max_sum = window_sum

for i in range(1, N - K + 1):
    window_sum = window_sum - temperatures[i - 1] + temperatures[i + K - 1]
    max_sum = max(max_sum, window_sum)

print(max_sum)
