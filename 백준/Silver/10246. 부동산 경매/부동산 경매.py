import sys

input = sys.stdin.readline

max_size = 1000000
count = [0] * (max_size + 1)


for k in range(1, max_size + 1):
    max_x = (max_size + 1 // k) + 1

    for x in range(2, max_x):
        total = x * k + (k * (k - 1)) // 2
        if total > max_size:
            break
        count[total] += 1

while True:
    N = int(input())
    if N == 0:
        break

    print(count[N])
