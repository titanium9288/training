def solution(num_list):
    return [even := sum(i%2 == 0 for i in num_list),len(num_list)-even]