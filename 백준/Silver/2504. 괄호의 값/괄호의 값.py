from collections import deque

stack = deque()
bracket_string = input()
result, calc = 0, 1

for i in range(len(bracket_string)):
    s = bracket_string[i]
    if s == "(":
        stack.append("(")
        calc *= 2
    if s == "[":
        stack.append("[")
        calc *= 3

    if s == ")":
        if len(stack) == 0 or stack[-1] != "(":
            result = 0
            break
        if bracket_string[i - 1] == "(":
            result += calc
        calc //= 2
        stack.pop()

    if s == "]":
        if len(stack) == 0 or stack[-1] != "[":
            result = 0
            break
        if bracket_string[i - 1] == "[":
            result += calc
        calc //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
