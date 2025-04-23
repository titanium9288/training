S, P = map(int, input().split())
DNA = input()
answer = 0

# Dictionary로 줄이기
require_values = list(map(int, input().split()))
require = {c: v for c, v in zip("ACGT", require_values)}

# 슬라이딩 윈도우
left, right = 0, P - 1
counter = {"ACGT"[i]: 0 for i in range(4)}

for i in range(P):
    counter[DNA[i]] += 1


while True:
    # 현재 문자열이 require에 충족하는지 확인
    for c in "ACGT":
        if counter[c] < require[c]:
            break
    else:
        answer += 1

    # break 조건을 중간에 넣어서 처음 문자열과 마지막 문자열 모두 탐색
    if right + 1 >= S:
        break

    counter[DNA[left]] -= 1
    left += 1
    right += 1
    counter[DNA[right]] += 1

print(answer)
