text = input()
bomb = list(input())
stack = []

for t in text:
    stack.append(t)

    if len(stack) < len(bomb):
        continue

    # indexing으로 bomb와 끝부분 비교 후, 일치하면 pop으로 제거
    # slice 보다 빠름
    for i in range(len(bomb)):
        if stack[-len(bomb) + i] != bomb[i]:
            break
    else:
        for _ in range(len(bomb)):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))
