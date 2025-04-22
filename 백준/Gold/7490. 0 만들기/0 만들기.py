def backtrack(paths, depth):

    if depth == N + 1:
        s = "".join(paths)
        if eval(s.replace(" ", "")) == 0:
            valid_expressions.append(s)
        return

    for op in (" ", "+", "-"):
        backtrack(paths + [op] + [str(depth)], depth + 1)


T = int(input())
for _ in range(T):
    N = int(input())
    valid_expressions = []

    backtrack(["1"], 2)
    print("\n".join(valid_expressions))
    print()
