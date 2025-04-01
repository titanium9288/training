from collections import deque
import sys

input = sys.stdin.readline


def make_DSLR(number):
    # DSLR 연산의 각 결과를 연산자-결과 쌍으로 만들어서 return
    result = {}
    result["D"] = (number * 2) % 10000
    result["S"] = number - 1 if number != 0 else 9999
    result["L"] = (number % 1000) * 10 + (number // 1000)
    result["R"] = (number % 10) * 1000 + (number // 10)
    return result


T = int(input())
is_visited = [""] * 10000

for i in range(T):
    start, target = map(int, input().split())

    # 경로를 직접 저장
    is_visited[:] = [""] * 10000
    queue = deque([start])

    # BFS
    while queue:
        current = queue.popleft()

        # 조건에 맞을 시 탐색 중단
        if current == target:
            print(is_visited[current])
            break

        for operator, next in make_DSLR(current).items():
            if current == next:
                continue
            if is_visited[next]:
                continue

            is_visited[next] = is_visited[current] + operator
            queue.append(next)
