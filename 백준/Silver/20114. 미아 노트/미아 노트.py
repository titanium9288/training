N, H, W = map(int, input().split())
restore_string = ["?"] * N


def restore_char(str):
    for c in str:
        if c != "?":
            return c
    return "?"


for _ in range(H):
    lines = input()

    for i in range(N):
        if restore_string[i] != "?":
            continue

        target = lines[i * W : (i + 1) * W]
        restore_string[i] = restore_char(target)

print("".join(restore_string))
