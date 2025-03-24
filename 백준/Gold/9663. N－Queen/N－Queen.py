N = int(input())
answer = 0


def backtrack(row, queens):
    global answer

    if len(queens) == N:
        answer += 1
        # visualize(queens)
        return

    # 절반탐색
    half = N
    if row == 0:
        half = N // 2

    for col in range(0, half):
        if is_safe(row, col, queens):
            queens.append(col)
            backtrack(row + 1, queens)
            queens.pop()


def is_safe(row, col, queens):
    for r, c in enumerate(queens):
        # 같은 행
        if row == r:
            return False
        # 같은 열
        if col == c:
            return False
        # 같은 대각선
        if abs(row - r) == abs(col - c):
            return False

    return True


def visualize(queens):
    for q in queens:
        print("".join("Q" if i == q else "." for i in range(N)))
    print()


backtrack(0, [])

# 홀수일 경우 N // 2 따로 처리
if N % 2 == 0:
    print(answer * 2)
else:
    answer_half = answer
    answer = 0
    backtrack(1, [N // 2])
    print(answer_half * 2 + answer)
