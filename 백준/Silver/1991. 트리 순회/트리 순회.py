from collections import defaultdict


def preorder(node):
    left, right = tree[node]

    print(node, end="")
    if left:
        preorder(left)
    if right:
        preorder(right)


def inorder(node):
    left, right = tree[node]

    if left:
        inorder(left)
    print(node, end="")
    if right:
        inorder(right)


def postorder(node):
    left, right = tree[node]

    if left:
        postorder(left)
    if right:
        postorder(right)
    print(node, end="")


N = int(input())
tree = defaultdict(list)

for i in range(N):
    node, left, right = input().split()

    left = None if left == "." else left
    right = None if right == "." else right

    tree[node] = [left, right]

# 전위
preorder("A")
print()

# 중위
inorder("A")
print()

# 후위
postorder("A")
