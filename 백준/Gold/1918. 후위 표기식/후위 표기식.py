def can_pop(top, current):
    if top == "(":
        return False
    return priority[top] >= priority[current]


operator = []
answer = []
priority = {"*": 2, "/": 2, "+": 1, "-": 1}

formula = input()

for i in formula:

    # 괄호 연산
    if i == "(":
        operator.append(i)
    elif i == ")":
        while True:
            j = operator.pop()
            if j == "(":
                break
            answer.append(j)

    # operator가 비어있을 경우 예외처리
    elif not operator and i in ("*", "/", "+", "-"):
        operator.append(i)

    # 연산 우선순위 고려하면서, while로 pop
    elif i in ("*", "/", "+", "-"):
        while operator and can_pop(operator[-1], i):
            answer.append(operator.pop())
        operator.append(i)

    # 피연산자
    else:
        answer.append(i)

# 남은 스택을 answer에 넣기
while operator:
    answer.append(operator.pop())

print("".join(answer))
