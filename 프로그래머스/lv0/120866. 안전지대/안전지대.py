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
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            
            # 해당 칸이 지뢰일 경우
            if board[row][col] == 1:
                for i in range(8):
                    new_row = row + dx[i]
                    new_col = col + dy[i]
                    
                    # 유효한 좌표 확인
                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                        if board[new_row][new_col] == 0:
                            board[new_row][new_col] = 2
                        
    counts = count_element(board)

    return counts.get(0, 0)
                
                        