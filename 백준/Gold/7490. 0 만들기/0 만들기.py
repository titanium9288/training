def backtrack(paths, depth):

    if depth == N + 1:
        formular = "".join(paths)
        if eval(formular.replace(" ", "")) == 0:
            able_formular.append(formular)
        return

    for op in (" ", "+", "-"):
        backtrack(paths + [op] + [str(depth)], depth + 1)


T = int(input())
for _ in range(T):
    N = int(input())
    able_formular = []

    backtrack(["1"], 2)
    print("\n".join(able_formular))
    print()