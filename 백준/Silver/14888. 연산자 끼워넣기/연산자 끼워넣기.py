def backtrack(path, visit):
    if len(path) == (N - 1):
        result = calculate(path)
        calculate_results.append(result)
        # print(result)
        return

    for i in range(len(op_list)):
        # 방문 했던 경우
        if visit[i]:
            continue

        # 앞에 사용한 op가 같은 op일 경우
        if i > 0 and op_list[i] == op_list[i - 1] and not visit[i - 1]:
            continue

        visit[i] = True
        backtrack(path + [op_list[i]], visit)
        visit[i] = False


def divider(a, b):
    if a < 0:
        return -(-a // b)
    else:
        return a // b


def calculate(op_order):
    result = numbers[0]

    for i in range(N - 1):
        op = op_order[i]
        if op == "+":
            result += numbers[i + 1]
        elif op == "-":
            result -= numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "/":
            result = divider(result, numbers[i + 1])

    return result


N = int(input())
numbers = list(map(int, input().split()))

op_symbol = ["+", "-", "*", "/"]
op_count = list(map(int, input().split()))
op_list = []

for i in range(4):
    op_list += [op_symbol[i]] * op_count[i]

calculate_results = []
backtrack([], [False] * len(op_list))

print(max(calculate_results))
print(min(calculate_results))
