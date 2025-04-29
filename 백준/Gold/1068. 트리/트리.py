from collections import deque


N = int(input())
tree = {i: set() for i in range(N)}
parents = list(map(int, input().split()))
root = 0

for i in range(N):
    parent = parents[i]

    if parents[i] == -1:
        root = i
        continue

    tree[parent].add(i)

delete_node = int(input())
delete_parent = parents[delete_node]
if delete_parent == -1:
    print(0)

else:
    tree[delete_parent].remove(delete_node)

    queue = deque([root])
    answer = 0

    while queue:
        current = queue.popleft()

        if not tree[current]:
            answer += 1

        for neighbors in tree[current]:
            queue.append(neighbors)

    print(answer)