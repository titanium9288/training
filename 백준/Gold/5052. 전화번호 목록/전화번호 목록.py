import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = sorted([input().strip() for _ in range(N)])

    for i in range(N - 1):
        if numbers[i + 1].startswith(numbers[i]):
            print("NO")
            break
    else:
        print("YES")
