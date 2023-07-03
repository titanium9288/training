N = int(input())
result = []

for i in range(N + 1):
    second = i
    number_list = [N, second]

    while True:
        number_list.append(number_list[-2] - number_list[-1])
        if number_list[-1] < 0:
            number_list.pop()
            break
    if len(result) <= len(number_list):
        result = number_list

print(len(result))
print(" ".join(map(str, result)))
