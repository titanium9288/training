from collections import deque


S = input()
T = input()

queue = deque([T])

# 상태 전이 BFS
while queue:
    current = queue.popleft()

    if current == S:
        print(1)
        break

    if len(current) < len(S):
        continue

    if current.endswith("A"):
        queue.append(current[:-1])
    if current.startswith("B"):
        queue.append(current[::-1][:-1])

else:
    print(0)
