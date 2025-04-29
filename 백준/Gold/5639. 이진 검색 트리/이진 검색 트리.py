import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(start, end):
    if start >= end:
        return

    root = preorder[start]

    # root보다 큰가 작은가를 기준으로 왼쪽, 오른쪽 나눠서 순회
    mid = start + 1
    while mid < end and preorder[mid] < root:
        mid += 1

    dfs(start + 1, mid)
    dfs(mid, end)
    postorder.append(str(root))


preorder = []
while True:
    n = input().strip()

    if n == "":
        break

    preorder.append(int(n))

postorder = []
dfs(0, len(preorder))

print("\n".join(postorder))
