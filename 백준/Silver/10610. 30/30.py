n = [int(i) for i in input()]

# 30의 배수의 조건
if sum(n) % 3 == 0 and 0 in n:
    n.sort(reverse=True)
    print(''.join(map(str, n)))

else:
    print(-1)