R, C = map(int, input().split())
grid = [input().rstrip() for _ in range(R)]

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_length = 0
max_length_limit = len(set("".join(grid)))

stack = [(0, 0, {grid[0][0]}, 1)]

while stack:
    r, c, path, level = stack.pop()

    if max_length < level:
        max_length = level
    if max_length == max_length_limit:
        break

    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        # 조건 함수를 인라인 처리로 빼기
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if grid[nr][nc] in path:
            continue

        new_path = path.copy()
        new_path.add(grid[nr][nc])
        stack.append((nr, nc, new_path, level + 1))

print(max_length)
