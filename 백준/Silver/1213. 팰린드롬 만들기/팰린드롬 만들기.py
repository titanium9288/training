from collections import Counter


def make_palindrome(name):
    count_letter = Counter(name)
    total = sum(count_letter.values())
    odd_count = sum(1 for value in count_letter.values() if value % 2 == 1)
    center = ""

    if total % 2:
        if odd_count != 1:
            return "I'm Sorry Hansoo"
        center = [key for key, value in count_letter.items() if value % 2 == 1][0]
        count_letter[center] -= 1
    else:
        if odd_count > 1:
            return "I'm Sorry Hansoo"

    half = "".join(key * (value // 2) for key, value in sorted(count_letter.items()))
    return half + center + half[::-1]


print(make_palindrome(input()))