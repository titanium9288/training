from collections import deque

def find_oil(land):
    row, col = len(land), len(land[0])
    
    visited = [[False for _ in range(col)] for _ in range(row)]
    queue = deque()
    oil_dict = {0 : 0}
    
    index = 2
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(row):
        for j in range(col):
            if visited[i][j] or land[i][j] == 0:
                continue
            
            visited[i][j] = True
            queue.append((i, j))

            size = 0

            while queue:
                size += 1
                x, y = queue.popleft()
                land[x][y] = index

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and land[nx][ny] != 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

            oil_dict[index] = size
            index += 1
        
    return oil_dict, land
                    
                
                

def solution(land):
    oil_dict, land = find_oil(land)
    row, col = len(land), len(land[0])
    answer = 0
    
    pipes = [set() for _ in range(col)]
    
    for i in range(row):
        for j in range(col):
            pipes[j].add(land[i][j])
    
    for pipe in pipes:
        answer = max(answer, sum(map(lambda x: oil_dict[x], pipe)))
    
    return answer