S = list(input())
T = list(input())

# S → T는 비결정적이지만,
# T → S는 유일한 방법을 추론할 수 있다.

while len(T) > len(S):
    last_added = T.pop()

    if last_added == "B":
        T = T[::-1]

print(int(T == S))