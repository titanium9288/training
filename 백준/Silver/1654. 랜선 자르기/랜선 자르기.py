import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
lan_list = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

low = 1
high = max(lan_list) + 1

while low < high:
    mid = (low + high) // 2
    guess = sum([lan // mid for lan in lan_list])

    if guess >= N:
        low = mid + 1
    else:
        high = mid

print(low - 1)
