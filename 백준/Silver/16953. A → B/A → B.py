from collections import deque

A, B = map(int, input().split())
queue = deque()

queue.append((A, 1))

while queue:
    current_value, step = queue.popleft()

    if current_value == B:
        print(step)
        break

    # 불가능한 경우
    if B < current_value:
        continue

    # 경로는 두가지로 제한. *2, *10 + 1
    queue.append((current_value * 2, step + 1))
    queue.append((current_value * 10 + 1, step + 1))
    
else:
    print(-1)
