from collections import Counter


N = int(input())
stick = list(map(int, input().split()))
fruits = Counter()

left, right = 0, 0
max_size = 0

while right < N:
    fruits[stick[right]] += 1

    while len(fruits) > 2:
        fruits[stick[left]] -= 1
        if fruits[stick[left]] == 0:
            del fruits[stick[left]]
        left += 1

    # print(stick[left : right + 1])
    size = right - left + 1
    if max_size < size:
        max_size = size

    right += 1

print(max_size)
