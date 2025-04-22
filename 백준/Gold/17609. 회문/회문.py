T = int(input())


def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return left, right
        left += 1
        right -= 1

    return None


for _ in range(T):
    s = input()

    # 안 맞는 지점에서의 left, right를 받아오기
    mismatch_point = is_palindrome(s, 0, len(s) - 1)

    if mismatch_point is None:
        print(0)
    else:
        left, right = mismatch_point

        # 둘 중 하나라도 회문이 성립한다면
        left_case = is_palindrome(s, left + 1, right)
        right_case = is_palindrome(s, left, right - 1)

        if left_case is None or right_case is None:
            print(1)
        else:
            print(2)
