A, B = map(int, input().split())

prefix_sum = [0]
n = 1
count = 0

while len(prefix_sum) <= B:
    prefix_sum.append(prefix_sum[-1] + n)

    count += 1
    if count == n:
        n += 1
        count = 0

print(prefix_sum[B] - prefix_sum[A - 1])
