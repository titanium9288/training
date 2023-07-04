def boy(n, switches):
    for i in range(n, len(switches) + 1, n):
        switches[i - 1] = 1 - switches[i - 1]
    return switches


def girl(n, switches):
    n = n - 1
    for i in range(0, len(switches)):
        if n - i < 0 or n + i >= len(switches):
            break

        if switches[n - i] == switches[n + i]:
            if i != 0:
                switches[n - i] = 1 - switches[n - i]
            switches[n + i] = 1 - switches[n + i]
        else:
            break

    return switches


N = int(input())
switches = list(map(int, input().split()))
for i in range(int(input())):
    student, num = map(int, input().split())
    if student == 1:
        boy(num, switches)
    else:
        girl(num, switches)


# 20개마다 줄바꿈
for i in range(len(switches)):
    print(switches[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
