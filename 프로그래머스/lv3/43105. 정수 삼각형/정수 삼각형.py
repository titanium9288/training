def solution(triangle):
    answer = [[triangle[0][0]]]
    for row in range(len(triangle) - 1):
        temp = []
        for col in range(len(triangle[row])):
            value1 = triangle[row+1][col] + answer[row][col]
            value2 = triangle[row+1][col+1] + answer[row][col]
            if temp:
                value1 = temp[-1] if temp[-1] > value1 else value1
                temp.pop()

            temp.append(value1)
            temp.append(value2)
            
        answer.append(temp)
        
    return max(answer[-1])