# 점프력, 시작 좌표, 끝 좌표
K, A, B = map(int, input().split())

# A나 B와 가장 가깝지만, 그보다는 작은 K의 배수
start = A - (A % K)
end = B - (B % K)
chocolate = 0

# 시작 지점에 초콜릿이 존재하는가?
if start == A:
    chocolate += 1

# 구간 내에 초콜릿이 존재할 수 있으려면, 시작점 + 점프력이 끝점보다 작거나 같아야 함
if end >= start + K:
    chocolate += (end - start) // K

print(chocolate)