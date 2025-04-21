def rotate_board(N, board):
    # N * 90도 회전한 board를 return
    rotated = board

    if N < 0:
        N += 4

    for _ in range(N):
        rotated = [list(reversed(col)) for col in zip(*rotated)]

    return rotated


def merge_board(direction, board):
    # direction은 각각 좌->상->우->하 순서로 돌아간다.

    new_board = []
    rotated = rotate_board(direction, board)

    for row in rotated:
        filtered_row = [x for x in row if x != 0]
        new_row = []
        i = 0

        while i < len(filtered_row):
            if i < len(filtered_row) - 1 and filtered_row[i] == filtered_row[i + 1]:
                new_row.append(filtered_row[i] * 2)
                i += 2
            else:
                new_row.append(filtered_row[i])
                i += 1

        new_board.append(new_row + [0] * (N - len(new_row)))

    return rotate_board(-direction, new_board)


def dfs(board, depth):
    result = max(map(max, board))

    # 최대 깊이 return
    if depth == 5:
        return result

    for direction in range(4):
        next_board = merge_board(direction, board)

        if next_board == board:
            continue

        result = max(result, dfs(next_board, depth + 1))

    return result


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

print(dfs(grid, 0))
