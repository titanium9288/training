N, len_S = map(int, input().split())
S = list(map(int, input().split()))

candidates = [i for i in range(1, 1002) if i not in S]
min_value = float("inf")

for x in candidates:
    for y in candidates:
        if y < x:
            continue

        xy = x * y
        if xy > N + min_value:
            break

        for z in candidates:
            if z < y:
                continue

            xyz = xy * z
            if xyz > N + min_value:
                break

            min_value = min(min_value, abs(N - xyz))

print(min_value)
