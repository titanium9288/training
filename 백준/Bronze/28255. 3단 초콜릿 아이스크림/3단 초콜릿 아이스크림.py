T = int(input())


def rev(S):
    return S[::-1]


def tail(S):
    return S[1:]


for _ in range(T):
    S = input()
    len_S = len(S)

    S_p = S[0 : (len_S + 2) // 3]
    # 경우의 수 나누기
    is_3dan = 0

    # S' + rev(S') + S'
    if len_S % 3 == 0:
        if S == S_p + rev(S_p) + S_p:
            is_3dan = 1

    # S' + tail(rev(S')) + tail(S')
    elif len_S % 3 == 1:
        if S == S_p + tail(rev(S_p)) + tail(S_p):
            is_3dan = 1

    # S' + tail(rev(S')) + S'
    # S' + rev(S') + tail(S')
    else:
        if S == S_p + tail(rev(S_p)) + S_p:
            is_3dan = 1
        elif S == S_p + rev(S_p) + tail(S_p):
            is_3dan = 1

    print(is_3dan)
