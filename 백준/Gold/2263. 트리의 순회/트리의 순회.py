import sys

sys.setrecursionlimit(10**6)


def dfs(in_start, in_end, post_start, post_end):
    if in_start >= in_end or post_start >= post_end:
        return

    root = postorder[post_end - 1]
    preorder.append(root)

    # root_idx = 0
    # for i in range(in_start, in_end):
    #     if inorder[i] == root:
    #         root_idx = i
    #         break
    root_idx = inorder_index[root]

    # postorder의 구간을 정의하기 위해서 위치 찾기
    left_size = root_idx - in_start

    dfs(in_start, root_idx, post_start, post_start + left_size)
    dfs(root_idx + 1, in_end, post_start + left_size, post_end - 1)


N = int(input())
inorder = list(map(int, input().split()))
inorder_index = {value: idx for idx, value in enumerate(inorder)}

postorder = list(map(int, input().split()))

preorder = []
dfs(0, N, 0, N)

print(*preorder)
