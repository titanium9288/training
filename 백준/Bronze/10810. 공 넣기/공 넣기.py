N, M = map(int, input().split())
basket = [0] * N

for i in range(M):
    start, end, ball = map(int, input().split())
    basket[start - 1 : end] = [ball] * (end - start + 1)

print(" ".join(map(str, basket)))