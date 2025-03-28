N, Q = map(int, input().split())
speed = list(map(int, input().split()))

prefix = [0]
for i in range(1, N):
    diff = abs(speed[i] - speed[i - 1])
    prefix.append(prefix[i - 1] + diff)

for _ in range(Q):
    start, end = map(int, input().split())
    print(prefix[end - 1] - prefix[start - 1])
