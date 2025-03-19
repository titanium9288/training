S = input()

order = 0
max_length = 0

for i in S:
    if i == "KOREA"[order]:
        order = (order + 1) % 5
        max_length += 1

print(max_length)
