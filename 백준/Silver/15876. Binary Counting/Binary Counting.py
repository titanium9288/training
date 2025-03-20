n, k = map(int, input().split())
numbers_seq = []
i = 0

while len(numbers_seq) < (n * 5 + k) + 1:
    numbers_seq += bin(i)[2:]
    i += 1

print(*(numbers_seq[k - 1 :: n][:5]))
