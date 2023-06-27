import sys

N = int(input())
input_seq = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

stack = []
stack_order = []
current_number = 1
is_possible = True

for i in input_seq:
    while current_number <= i:
        stack.append(current_number)
        stack_order.append("+")
        current_number += 1
    if stack and stack[-1] == i:
        stack.pop()
        stack_order.append("-")
    else:
        is_possible = False

if is_possible:
    print("\n".join(stack_order))
else:
    print("NO")
