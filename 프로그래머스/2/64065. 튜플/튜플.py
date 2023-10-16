def count_elements_to_list(lst):
    count_dict = {}
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1

    sorted_list = sorted(count_dict, key=lambda x: count_dict[x], reverse=True)
    return sorted_list

def str_to_list(s):
    return s.replace("{", '').replace("}", '').split(',')

def solution(s):
    elements_list = count_elements_to_list(str_to_list(s))
    return list(map(int, elements_list))