from collections import deque


T = int(input())

for i in range(T):
    # 문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서 M
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    index_list = list(range(len(importance)))

    importance_queue = deque(zip(importance, index_list))
    current_order = 0

    while True:
        current_paper = importance_queue.popleft()

        # 큐가 비어있는 경우
        if len(importance_queue) == 0:
            current_order += 1
            print(current_order)
            break

        if max(importance_queue)[0] > current_paper[0]:
            # 중요도가 큰 문서가 있을 때 뒤에 재배치
            importance_queue.append(current_paper)
            continue

        current_order += 1
        if current_paper[1] == M:
            print(current_order)
            break