def count_element(list):
    counts = {}
    
    for j in list:
        for i in j:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
    return counts


def solution(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            
            # 해당 칸이 지뢰일 경우
            if board[row][col] == 1:
                for dx, dy in [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
                    new_row = row + dx
                    new_col = col + dy
                    
                    # 유효한 좌표 확인
                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                        if board[new_row][new_col] == 0:
                            board[new_row][new_col] = 2
                        
    counts = count_element(board)

    return counts.get(0, 0)
                
                        