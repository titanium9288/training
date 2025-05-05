T = int(input())
button_times = [300, 60, 10]
click_count = [0, 0, 0]


while T != 0:
    for i in range(3):
        if T >= button_times[i]:
            T -= button_times[i]
            click_count[i] += 1
            break

    if T % 10:
        print(-1)
        break
else:
    print(*click_count)
