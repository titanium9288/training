from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# DFS
def dfs(curr):
    # 메모이제이션
    if dp[curr] != -1:
        return

    if not graph[curr]:
        dp[curr] = time[curr]
        return

    for prev in graph[curr]:
        if dp[prev] != -1:
            continue

        dfs(prev)

    dp[curr] = max(map(lambda x: dp[x], graph[curr])) + time[curr]


T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    dp = [0] + [-1] * N
    graph = defaultdict(list)

    # 그래프에 순서를 반대로 담으면 백트래킹 하기 편해보임
    for _ in range(K):
        prev, curr = map(int, input().split())
        graph[curr].append(prev)

    W = int(input())
    dfs(W)
    print(max(dp))
