def backtrack(board, idx):
    if idx == len(blank_cell):
        return board

    r, c = blank_cell[idx]
    b = (r // 3) * 3 + (c // 3)

    filterd_number = [i for i in range(1, 10) if row[r][i] and col[c][i] and box[b][i]]

    for i in filterd_number:
        board[r][c] = i
        row[r][i], col[c][i], box[b][i] = False, False, False

        completed_board = backtrack(board, idx + 1)
        if completed_board:
            return completed_board

        row[r][i], col[c][i], box[b][i] = True, True, True
        board[r][c] = 0


row = [[True] * 10 for _ in range(9)]
col = [[True] * 10 for _ in range(9)]
box = [[True] * 10 for _ in range(9)]

N = 9
grid = [list(map(int, list(input()))) for _ in range(N)]

blank_cell = []
visited = set()

for r in range(N):
    for c in range(N):
        if grid[r][c] == 0:
            blank_cell.append((r, c))
        else:
            n = grid[r][c]
            b = (r // 3) * 3 + (c // 3)
            row[r][n] = False
            col[c][n] = False
            box[b][n] = False

result = backtrack(grid, 0)

for row in result:
    print("".join(map(str, row)))
