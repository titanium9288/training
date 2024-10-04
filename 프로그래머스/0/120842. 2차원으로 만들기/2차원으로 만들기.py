def solution(num_list, n):
    answer = [[num_list[j] for j in range(i*n, i*n+n)] for i in range(len(num_list) // n)]
    return answer