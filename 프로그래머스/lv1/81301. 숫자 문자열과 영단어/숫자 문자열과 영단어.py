def solution(s):
    answer = s
    number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(number_list)):
        answer = answer.replace(number_list[i], str(i))
    return int(answer)