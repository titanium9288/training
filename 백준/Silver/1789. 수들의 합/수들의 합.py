N = int(input())
i = 0

# 가우스 합
while (i*(i+1))//2 <= N:
    i += 1

print(i - 1)